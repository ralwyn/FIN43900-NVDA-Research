"""Lab 09 ABG teaching case. USD millions except per-share value.

Source: supplied lab-09-proforma-build.md; inputs are course assumptions,
not independently verified current company data. Standard library only.
Run normally, or use --break-2026-cash to demonstrate valuation refusal.
"""
import argparse

ASSUMPTIONS = {
    'growth': (0.018, 'judgment'),
    'gross_margin': (0.1705, 'judgment'),
    'sga_ratios': ((0.665, 0.655, 0.645, 0.645, 0.645), 'judgment'),
    'depreciation_ratio': (82.4 / 3070.4, 'history'),
    'impairment': (120.0, 'judgment'),
    'capex': (250.0, 'guidance'),
    'tax_rate': (0.255, 'judgment'),
    'inventory_days': (2135.8 / (17999.0 - 3071.7) * 365, 'history'),
    'floor_plan_ratio': (2027.0 / 2135.8, 'history'),
    'other_wc_ratio': (0.008, 'judgment'),
    'minimum_cash': (25.0, 'history'),
    'revolver_limit': (850.0, 'judgment'),
    'revolver_rate': (0.06, 'judgment'),
    'repayment': (150.0, 'judgment'),
    'buyback': (150.0, 'judgment'),
    'floor_plan_rate': (0.0467, 'history'),
    'debt_rate': (0.0544, 'history'),
    'cost_of_equity': (0.10, 'judgment'),
    'terminal_growth': (0.025, 'judgment'),
    'shares': (17.951349, 'fact: course cites June 30, 2026 10-Q'),
}
OPENING = dict(revenue=17999.0, inventory=2135.8, ppe=3070.4,
               other_assets=6371.6, cash=40.4, floor_plan=2027.0,
               debt=3572.0, other_liabilities=2127.5, equity=3891.7,
               revolver=0.0)
A = {key: item[0] for key, item in ASSUMPTIONS.items()}


def project(break_cash=False):
    prior = OPENING.copy()
    rows = []
    for i, year in enumerate(range(2026, 2031)):
        r = {'year': year, 'opening_cash': prior['cash']}
        r['revenue'] = prior['revenue'] * (1 + A['growth'])
        r['gross_profit'] = r['revenue'] * A['gross_margin']
        r['cogs'] = r['revenue'] - r['gross_profit']
        r['sga'] = r['gross_profit'] * A['sga_ratios'][i]
        r['depreciation'] = prior['ppe'] * A['depreciation_ratio']
        r['impairment'] = A['impairment']
        r['operating_income'] = r['gross_profit'] - r['sga'] - r['depreciation'] - r['impairment']
        r['interest'] = (prior['floor_plan'] * A['floor_plan_rate']
                         + prior['debt'] * A['debt_rate']
                         + prior['revolver'] * A['revolver_rate'])
        r['pretax'] = r['operating_income'] - r['interest']
        r['tax'] = max(0, r['pretax']) * A['tax_rate']
        r['net_income'] = r['pretax'] - r['tax']
        r['inventory'] = r['cogs'] * A['inventory_days'] / 365
        r['floor_plan'] = r['inventory'] * A['floor_plan_ratio']
        r['capex'] = A['capex']
        r['ppe'] = prior['ppe'] + r['capex'] - r['depreciation']
        r['change_other_wc'] = A['other_wc_ratio'] * (r['revenue'] - prior['revenue'])
        r['other_assets'] = prior['other_assets'] + r['change_other_wc'] - r['impairment']
        r['repayment'] = A['repayment']
        r['debt'] = prior['debt'] - r['repayment']
        r['other_liabilities'] = prior['other_liabilities']
        r['buyback'] = A['buyback']
        r['equity'] = prior['equity'] + r['net_income'] - r['buyback']
        r['change_inventory'] = r['inventory'] - prior['inventory']
        r['change_floor_plan'] = r['floor_plan'] - prior['floor_plan']
        r['operating_cash_flow'] = (r['net_income'] + r['depreciation'] + r['impairment']
                                    - r['change_inventory'] - r['change_other_wc']
                                    + r['change_floor_plan'])
        r['fcfe'] = r['operating_cash_flow'] - r['capex'] - r['repayment']
        cash_before_revolver = prior['cash'] + r['fcfe'] - r['buyback']
        if cash_before_revolver < A['minimum_cash']:
            change_revolver = min(A['minimum_cash'] - cash_before_revolver,
                                  A['revolver_limit'] - prior['revolver'])
        else:
            change_revolver = -min(prior['revolver'], cash_before_revolver - A['minimum_cash'])
        r['change_revolver'] = change_revolver
        r['revolver'] = prior['revolver'] + change_revolver
        r['cash_change'] = r['fcfe'] - r['buyback'] + change_revolver
        r['cf_ending_cash'] = prior['cash'] + r['cash_change']
        r['cash'] = r['cf_ending_cash']
        if break_cash and year == 2026:
            r['cash'] = OPENING['cash']
        r['assets'] = r['cash'] + r['inventory'] + r['ppe'] + r['other_assets']
        r['liabilities'] = r['floor_plan'] + r['debt'] + r['other_liabilities'] + r['revolver']
        r['balance_gap'] = r['assets'] - r['liabilities'] - r['equity']
        r['cash_gap'] = r['cash'] - r['cf_ending_cash']
        rows.append(r)
        prior = r
    return rows


def assert_balanced(rows):
    for r in rows:
        for key, label in [('balance_gap', 'assets minus liabilities minus equity'),
                           ('cash_gap', 'balance-sheet cash minus cash-flow cash')]:
            if abs(r[key]) > 1e-7:
                raise ValueError(f"FY{r['year']}E: {label} gap {r[key]:.1f}; valuation refused")
        if r['cash'] < A['minimum_cash'] - 1e-7:
            raise ValueError(f"FY{r['year']}E: minimum-cash gap {r['cash'] - A['minimum_cash']:.1f}; valuation refused")
        if not -1e-7 <= r['revolver'] <= A['revolver_limit'] + 1e-7:
            raise ValueError(f"FY{r['year']}E: revolver outside limit; valuation refused")


def table(title, rows, fields):
    print('\n' + title + ' (USD millions)')
    print(f"{'Line':<31}" + ''.join(f"{str(r['year']) + 'E':>13}" for r in rows))
    for key, label in fields:
        print(f'{label:<31}' + ''.join(f'{(0 if abs(r[key]) < 1e-7 else r[key]):>13,.1f}' for r in rows))


def value(rows):
    assert_balanced(rows)
    k, g = A['cost_of_equity'], A['terminal_growth']
    if k <= g:
        raise ValueError('Cost of equity must exceed terminal growth')
    pv_fcfe = sum(r['fcfe'] / (1 + k) ** (i + 1) for i, r in enumerate(rows))
    terminal = (rows[-1]['fcfe'] + rows[-1]['repayment']) * (1 + g) / (k - g)
    pv_terminal = terminal / (1 + k) ** len(rows)
    equity = pv_fcfe + pv_terminal
    return equity, pv_terminal / equity, equity / A['shares']


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--break-2026-cash', action='store_true')
    args = parser.parse_args()
    rows = project(args.break_2026_cash)
    table('CHECK BLOCK', rows, [('balance_gap', 'Assets - liabilities - equity'), ('cash_gap', 'BS cash - cash-flow cash')])
    print('Cash >= minimum:               ' + ''.join(f"{str(r['cash'] >= A['minimum_cash'] - 1e-7):>13}" for r in rows))
    table('INCOME STATEMENT', rows, [(k, label) for k, label in [
        ('revenue', 'Revenue'), ('cogs', 'Cost of sales'), ('gross_profit', 'Gross profit'),
        ('sga', 'SG&A'), ('depreciation', 'Depreciation'), ('impairment', 'Impairment'),
        ('operating_income', 'Operating income'), ('interest', 'Interest'), ('pretax', 'Pretax income'),
        ('tax', 'Tax'), ('net_income', 'Net income')]])
    table('BALANCE SHEET', rows, [(k, k.replace('_', ' ').title()) for k in [
        'cash', 'inventory', 'ppe', 'other_assets', 'assets', 'floor_plan', 'debt',
        'revolver', 'other_liabilities', 'liabilities', 'equity']])
    table('CASH FLOW', rows, [(k, k.replace('_', ' ').title()) for k in [
        'net_income', 'depreciation', 'impairment', 'change_inventory', 'change_other_wc',
        'change_floor_plan', 'operating_cash_flow', 'capex', 'repayment', 'fcfe', 'buyback',
        'change_revolver', 'cash_change', 'opening_cash', 'cf_ending_cash']])
    print('Cash-flow convention: capex, repayment, buyback and increases in inventory/other WC are subtracted.')
    equity, terminal_share, per_share = value(rows)
    print(f'\nEquity value (USD millions): {equity:,.2f}')
    print(f'Share of value after 2030: {terminal_share:.2%}')
    print(f'Value per share: ${per_share:.2f}')


if __name__ == '__main__':
    main()
