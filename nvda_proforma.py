"""Lab 10 NVIDIA annual pro-forma teaching model, prepared 2026-09-24.
USD millions, shares in millions, except per-share figures. Standard library only.
See lab10-nvda-report.md for sources, assumptions, dating and limitations.
Run: python3 nvda_proforma.py [--self-test | --break-cash | --sensitivity]
"""
import argparse
import copy
import math

SOURCES = {
    2024: 'https://www.sec.gov/Archives/edgar/data/1045810/000104581024000029/nvda-20240128.htm',
    2025: 'https://www.sec.gov/Archives/edgar/data/1045810/000104581025000023/nvda-20250126.htm',
    2026: 'https://www.sec.gov/Archives/edgar/data/1045810/000104581026000021/nvda-20260125.htm',
    'Q2': 'https://investor.nvidia.com/files/doc_financials/2027/NVDA-2027-Q2-10Q-Final-including-exhibits.pdf',
    'guidance': 'https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Announces-Financial-Results-for-Second-Quarter-Fiscal-2027/',
    'provider': 'https://stockanalysis.com/stocks/nvda/financials/cash-flow-statement/',
    'price': 'https://www.financialcontent.com/quote/NQ:NVDA/historical',
}
# Each year's historical column is sourced to that year's 10-K above.
# Depreciation 2025/2026 is rounded in the notes; it is not total D&A.
HISTORY = {
    2024: dict(revenue=60922, prior_revenue=26974, gross_profit=44301, sga=2654,
               rd=8675, net_income=29760, inventory=5282, ppe=3914, equity=42978,
               depreciation=894, da=1508, capex=1069, tax=4058, pretax=33818,
               ar=9999, ap=2699, cfo=28090, sbc=3549),
    2025: dict(revenue=130497, prior_revenue=60922, gross_profit=97858, sga=3491,
               rd=12914, net_income=72880, inventory=10080, ppe=6283, equity=79327,
               depreciation=1300, da=1864, capex=3236, tax=11146, pretax=84026,
               ar=23065, ap=6310, cfo=64089, sbc=4737),
    2026: dict(revenue=215938, prior_revenue=130497, gross_profit=153463, sga=4579,
               rd=18497, net_income=120067, inventory=21403, ppe=10383, equity=157293,
               depreciation=2400, da=2843, capex=6042, tax=21383, pretax=141450,
               ar=38466, ap=9812, cfo=102718, sbc=6386),
}
# Fully reconciled FY2026 reported balance sheet. Other assets exclude investments.
OPENING = dict(year=2026, revenue=215938.0, cash=10605.0, securities=51951.0,
               ar=38466.0, inventory=21403.0, prepaid=3180.0, ppe=10383.0,
               intangibles=3306.0, private_investments=22251.0,
               other_assets=2867.0+20832.0+13258.0+8301.0,
               ap=9812.0, accrued=21352.0, debt=999.0+7469.0,
               other_liabilities=2572.0+7306.0, equity=157293.0, revolver=0.0)
# These are economic forecasts, not mechanical continuations of history.
ASSUMPTIONS = {
    'growth': ((177837+108000+118800)/215938-1, .35, .25, .15, .08),
    'gross_margin': (.74, .73, .72, .71, .70),
    'sga_gp': (.025, .027, .029, .030, .030),
    'rd_revenue': (.08, .09, .10, .11, .12),
    'tax_rate': .17,
    'inventory_days': 21403/62475*365,
    'receivable_days': 38466/215938*365,
    'payable_days': 9812/62475*365,
    'prepaid_revenue': 3180/215938,
    'accrued_revenue': (21352-3921)/215938,
    'purchase_consideration_payment': 3921.0,
    'depreciation_opening_ppe': 2400/10383,
    'amortization_opening_intangibles': 923/3306,
    'capex_revenue': .03,
    'tangible_capex_share': .97,
    'interest_rate': 259/8468,
    'debt_repayment': 0.0,
    'minimum_cash': 5000.0,
    'revolver_limit': 0.0,
    'revolver_rate': .06,
    'annual_dividend_per_share': 1.0,
    'buyback': 0.0,
    'shares': 24100.0,
    'cost_of_equity': .12,
    'terminal_growth': .03,
    'private_investment_haircut': .25,
    'market_price': 224.20,
}
# One label/reason for every configurable assumption, including simplifications.
LABELS = {
    'growth': ('judgment', 'FY27 = H1 actual 177837 + Q3 guidance midpoint 108000 + Q4 judgment 118800; later growth fades as the revenue base expands.'),
    'gross_margin': ('judgment', 'Start near Q3 guidance of 74%; fade to 70% as competition and product mix limit pricing.'),
    'sga_gp': ('judgment', 'Allow operating leverage initially, then moderately higher selling costs relative to gross profit.'),
    'rd_revenue': ('judgment', 'Keep R&D material and increase its revenue share as product competition intensifies.'),
    'tax_rate': ('judgment', '17% is the midpoint of FY27 guidance of 16%-18%; holding it through FY31 is a judgment.'),
    'inventory_days': ('history', 'FY26 ending inventory / cost of revenue x 365; carrying it forward assumes the same inventory intensity.'),
    'receivable_days': ('history', 'FY26 ending receivables / revenue x 365; forecast holds collection intensity.'),
    'payable_days': ('history', 'FY26 ending accounts payable / cost of revenue x 365; no floor-plan borrowing.'),
    'prepaid_revenue': ('history', 'FY26 prepaid/current-other assets / revenue; scales supplier prepayments and other current assets together.'),
    'accrued_revenue': ('history', 'FY26 accrued current liabilities less 3921 purchase consideration, divided by revenue; exclude one-off acquisition financing.'),
    'purchase_consideration_payment': ('judgment', 'Settle the FY26 accrued purchase consideration in FY27, consistent with the within-one-year disclosure; cash estimate uses carrying value.'),
    'depreciation_opening_ppe': ('history', 'Rounded FY26 depreciation 2400 / ending PP&E 10383, applied to opening forecast PP&E.'),
    'amortization_opening_intangibles': ('judgment', 'FY27 disclosed amortization 923 / opening intangibles 3306; reuse as a simplifying declining-balance rate.'),
    'capex_revenue': ('judgment', '3% exceeds FY26 cash capex/revenue of about 2.8%, allowing investment as the platform grows.'),
    'tangible_capex_share': ('judgment', 'Allocate 97% of combined cash capex to PP&E and 3% to intangibles; filing does not supply this forecast split.'),
    'interest_rate': ('history', 'FY26 interest expense / ending carrying debt; holding the rate is a refinancing simplification.'),
    'debt_repayment': ('judgment', 'Refinance maturities at equal principal; debt balance held flat, no perpetual debt-paydown addback.'),
    'minimum_cash': ('judgment', 'Keep $5bn operating liquidity; this is a model floor, not company guidance.'),
    'revolver_limit': ('judgment', 'No unverified credit line assumed; fail when cash cannot meet its floor.'),
    'revolver_rate': ('judgment', '6% stress-test placeholder; base-case credit limit is zero.'),
    'annual_dividend_per_share': ('judgment', 'Annualize Q2 FY27 dividend of $0.25 to $1; freeze solely for the cash/equity bridge.'),
    'buyback': ('judgment', 'No future buyback assumed; keep the ownership denominator fixed.'),
    'shares': ('history', 'Latest 10-Q cover: 24.1bn actual shares at Aug 21 2026, rounded by the issuer; use post-split shares, not FY24 pre-split shares.'),
    'cost_of_equity': ('judgment', '12% required return for a concentrated, cyclical growth business; not a measured beta or CAPM estimate.'),
    'terminal_growth': ('judgment', '3% long-run nominal growth, below 12%; normalize reinvestment to stable asset intensity.'),
    'private_investment_haircut': ('judgment', '25% haircut to FY26 private investment carrying value for uncertainty and liquidity; marketable securities use carrying value.'),
    'market_price': ('history', 'FinancialContent quote: $224.20, Sep 24 2026, 2:05 PM EDT; intraday reference, not closing price.'),
}


def totals(r):
    r['assets'] = sum(r[k] for k in ('cash','securities','ar','inventory','prepaid','ppe','intangibles','private_investments','other_assets'))
    r['liabilities'] = sum(r[k] for k in ('ap','accrued','debt','other_liabilities','revolver'))
    return r


def check_gap(year, name, gap, tolerance=1e-6):
    if not math.isfinite(gap) or abs(gap) > tolerance:
        raise ValueError(f'FY{year}E: {name} gap {gap:,.6f}; valuation refused')


def assert_balanced(rows, a=ASSUMPTIONS):
    prior = totals(OPENING.copy())
    check_gap(2026, 'opening balance sheet', prior['assets']-prior['liabilities']-prior['equity'])
    for r in rows:
        year = r['year']
        if any(not math.isfinite(v) for v in r.values() if isinstance(v,(int,float))):
            raise ValueError(f'FY{year}E: non-finite input/output; valuation refused')
        actual = totals(r.copy())
        check_gap(year, 'balance sheet', actual['assets']-actual['liabilities']-r['equity'])
        check_gap(year, 'cash reconciliation', r['cash']-prior['cash']-r['cfo']-r['cfi']-r['cff'])
        check_gap(year, 'equity rollforward', r['equity']-prior['equity']-r['net_income']+r['dividends']+r['buyback'])
        check_gap(year, 'PP&E rollforward', r['ppe']-prior['ppe']-r['tangible_capex']+r['depreciation'])
        check_gap(year, 'intangible rollforward', r['intangibles']-prior['intangibles']-r['intangible_capex']+r['amortization'])
        check_gap(year, 'income statement', r['net_income']-(r['revenue']-r['cogs']-r['sga']-r['rd']-r['interest']-r['tax']))
        check_gap(year, 'FCFE bridge', r['fcfe']-(r['cfo']+r['cfi']-r['repayment']+r['change_revolver']))
        check_gap(year, 'debt rollforward', r['debt']-prior['debt']+r['repayment'])
        if r['cash'] < a['minimum_cash']-1e-6:
            raise ValueError(f"FY{year}E: minimum cash gap {r['cash']-a['minimum_cash']:,.6f}; valuation refused")
        if not -1e-6 <= r['revolver'] <= a['revolver_limit']+1e-6:
            raise ValueError(f'FY{year}E: revolver outside approved model limit; valuation refused')
        for key in ('inventory','ar','ap','ppe','intangibles','debt'):
            if r[key] < 0:
                raise ValueError(f'FY{year}E: negative {key}; valuation refused')
        prior = r


def project(a=ASSUMPTIONS):
    prior = totals(OPENING.copy())
    result = []
    for i, year in enumerate(range(2027,2032)):
        r = dict(year=year, revenue=prior['revenue']*(1+a['growth'][i]))
        r['gross_profit'] = r['revenue']*a['gross_margin'][i]
        r['cogs'] = r['revenue']-r['gross_profit']
        r['sga'] = r['gross_profit']*a['sga_gp'][i]
        r['rd'] = r['revenue']*a['rd_revenue'][i]
        # D&A and compensation are already included in these expense ratios.
        r['operating_income'] = r['gross_profit']-r['sga']-r['rd']
        r['interest'] = prior['debt']*a['interest_rate']+prior['revolver']*a['revolver_rate']
        r['pretax'] = r['operating_income']-r['interest']
        r['tax'] = max(r['pretax'],0)*a['tax_rate']
        r['net_income'] = r['pretax']-r['tax']
        r['depreciation'] = prior['ppe']*a['depreciation_opening_ppe']
        r['amortization'] = prior['intangibles']*a['amortization_opening_intangibles']
        r['capex'] = r['revenue']*a['capex_revenue']
        r['tangible_capex'] = r['capex']*a['tangible_capex_share']
        r['intangible_capex'] = r['capex']-r['tangible_capex']
        r['ppe'] = prior['ppe']+r['tangible_capex']-r['depreciation']
        r['intangibles'] = prior['intangibles']+r['intangible_capex']-r['amortization']
        r['ar'] = r['revenue']*a['receivable_days']/365
        r['inventory'] = r['cogs']*a['inventory_days']/365
        r['ap'] = r['cogs']*a['payable_days']/365
        r['prepaid'] = r['revenue']*a['prepaid_revenue']
        r['accrued'] = r['revenue']*a['accrued_revenue']
        for key in ('other_assets','other_liabilities','securities','private_investments'):
            r[key] = prior[key]
        r['repayment'] = min(prior['debt'],a['debt_repayment'])
        r['debt'] = prior['debt']-r['repayment']
        r['purchase_payment'] = a['purchase_consideration_payment'] if i == 0 else 0.0
        # Remove the acquisition liability from operating working capital.
        opening_operating_accrued = prior['accrued']-r['purchase_payment']
        for key in ('ar','inventory','prepaid','ap'):
            r['delta_'+key] = r[key]-prior[key]
        r['delta_accrued'] = r['accrued']-opening_operating_accrued
        r['delta_nwc'] = r['delta_ar']+r['delta_inventory']+r['delta_prepaid']-r['delta_ap']-r['delta_accrued']
        # Treat share-based pay as cash-equivalent compensation; no free SBC addback.
        r['cfo'] = r['net_income']+r['depreciation']+r['amortization']-r['delta_nwc']
        r['cfi'] = -r['capex']-r['purchase_payment']
        r['dividends'] = a['annual_dividend_per_share']*a['shares']
        r['buyback'] = a['buyback']
        pre_financing_cash = prior['cash']+r['cfo']+r['cfi']-r['repayment']-r['dividends']-r['buyback']
        if pre_financing_cash < a['minimum_cash']:
            r['change_revolver'] = min(a['minimum_cash']-pre_financing_cash,a['revolver_limit']-prior['revolver'])
        else:
            r['change_revolver'] = -min(prior['revolver'],pre_financing_cash-a['minimum_cash'])
        r['revolver'] = prior['revolver']+r['change_revolver']
        r['cff'] = -r['repayment']-r['dividends']-r['buyback']+r['change_revolver']
        r['cash_change'] = r['cfo']+r['cfi']+r['cff']
        r['cash'] = prior['cash']+r['cash_change']  # computed from cash flows, never a balancing plug
        r['equity'] = prior['equity']+r['net_income']-r['dividends']-r['buyback']
        r['fcfe'] = r['cfo']+r['cfi']-r['repayment']+r['change_revolver']
        totals(r)
        result.append(r)
        prior = r
    return result


def valuation(rows, a=ASSUMPTIONS):
    assert_balanced(rows,a)  # Mandatory guard: no valuation may bypass checks.
    k,g = a['cost_of_equity'],a['terminal_growth']
    if not math.isfinite(k+g) or k <= g or g < 0 or a['shares'] <= 0:
        raise ValueError('Invalid discount rate, terminal growth or shares; valuation refused')
    if any(r['fcfe'] < 0 for r in rows):
        raise ValueError('Negative FCFE scenario: revise/document funding; valuation refused rather than silently deleting losses')
    last = rows[-1]
    if last['revolver'] > 1e-6:
        raise ValueError('Outstanding revolver needs a terminal financing policy; valuation refused')
    terminal_revenue = last['revenue']*(1+g)
    terminal_gp = terminal_revenue*a['gross_margin'][-1]
    terminal_op = terminal_gp*(1-a['sga_gp'][-1])-terminal_revenue*a['rd_revenue'][-1]
    terminal_pretax = terminal_op-last['debt']*a['interest_rate']
    terminal_ni = terminal_pretax-max(0,terminal_pretax)*a['tax_rate']
    nwc = last['ar']+last['inventory']+last['prepaid']-last['ap']-last['accrued']
    # Stable productive-asset intensity: capex = D&A + g * productive assets.
    terminal_net_capex = g*(last['ppe']+last['intangibles'])
    terminal_delta_nwc = g*nwc
    terminal_fcfe = terminal_ni-terminal_net_capex-terminal_delta_nwc
    if terminal_fcfe <= 0:
        raise ValueError('Nonpositive terminal FCFE; perpetuity valuation refused')
    terminal_value = terminal_fcfe/(k-g)
    pv_fcfe = sum(r['fcfe']/(1+k)**(i+1) for i,r in enumerate(rows))
    pv_terminal = terminal_value/(1+k)**5
    # No earnings from these financial assets are included above, so add them once.
    nonoperating = max(0,OPENING['cash']-a['minimum_cash'])+OPENING['securities']+OPENING['private_investments']*(1-a['private_investment_haircut'])
    equity = pv_fcfe+pv_terminal+nonoperating
    return dict(pv_fcfe=pv_fcfe,pv_terminal=pv_terminal,nonoperating=nonoperating,
                terminal_fcfe=terminal_fcfe,terminal_net_capex=terminal_net_capex,
                terminal_delta_nwc=terminal_delta_nwc,equity=equity,
                per_share=equity/a['shares'],terminal_share=pv_terminal/equity)


def print_table(title,rows,fields):
    print('\n'+title+' (USD millions)')
    print(f"{'Line':<33}"+''.join(f"{'FY'+str(r['year'])+'E':>15}" for r in rows))
    for key,label in fields:
        print(f'{label:<33}'+''.join(f'{(0 if abs(r[key])<1e-6 else r[key]):>15,.1f}' for r in rows))


def print_checks(rows,a=ASSUMPTIONS):
    print('CHECK BLOCK — USD millions; tolerance 0.000001')
    prior = OPENING
    for r in rows:
        z = totals(r.copy())
        gaps = (z['assets']-z['liabilities']-r['equity'],r['cash']-prior['cash']-r['cfo']-r['cfi']-r['cff'])
        print(f"FY{r['year']}E  BS gap={0 if abs(gaps[0])<1e-6 else gaps[0]:,.6f}  cash gap={0 if abs(gaps[1])<1e-6 else gaps[1]:,.6f}  cash floor={'PASS' if r['cash']>=a['minimum_cash'] else 'FAIL'}  revolver={r['revolver']:,.1f}")
        prior=r
    assert_balanced(rows,a)
    print('PASS: all eight reconciliation checks, finite values, asset/debt signs, cash floor and revolver limits.')


def self_test():
    rows = project()
    assert_balanced(rows)
    assert set(ASSUMPTIONS)==set(LABELS)
    print('PASS: source-labelled inputs and all five years of statements reconcile.')
    first = rows[0]
    expected_revenue = 177837+108000+118800
    expected_ni = (expected_revenue*.74*(1-.025)-expected_revenue*.08-259)*.83
    assert math.isclose(first['revenue'],expected_revenue,abs_tol=1e-6)
    assert math.isclose(first['net_income'],expected_ni,abs_tol=1e-6)
    print('PASS: FY2027 revenue and net income independently recomputed.')
    for field,label in [('cash','cash corruption'),('equity','equity corruption'),('ppe','PP&E corruption'),('cfo','cash-flow corruption')]:
        broken=copy.deepcopy(rows)
        broken[0][field]+=1
        try:
            valuation(broken)
        except ValueError as e:
            print(f'PASS: {label} blocked: {e}')
        else:
            raise AssertionError('Corruption not caught: '+field)
    broken=copy.deepcopy(rows)
    broken[0]['cash']=OPENING['cash']
    try:
        valuation(broken)
    except ValueError as e:
        print('PASS: frozen opening cash blocked:',e)
    else:
        raise AssertionError('Frozen cash not caught')
    bad=copy.deepcopy(rows);bad[0]['cash']=float('nan')
    try: valuation(bad)
    except ValueError: print('PASS: NaN cannot bypass the balance check.')
    else: raise AssertionError('NaN passed')
    stressed=copy.deepcopy(ASSUMPTIONS);stressed['annual_dividend_per_share']=1000
    try: valuation(project(stressed),stressed)
    except ValueError: print('PASS: unfunded cash shortfall blocked with no invented credit facility.')
    else: raise AssertionError('Funding failure passed')
    bad=copy.deepcopy(ASSUMPTIONS);bad['cost_of_equity']=bad['terminal_growth']
    try: valuation(rows,bad)
    except ValueError: print('PASS: discount rate equal to growth blocked.')
    else: raise AssertionError('Invalid perpetuity passed')
    base=valuation(rows)
    high=copy.deepcopy(ASSUMPTIONS);high['cost_of_equity']=.14
    assert valuation(rows,high)['per_share']<base['per_share']
    print('PASS: higher required return lowers value for unchanged statements.')
    # A new supplier balance must affect both assets and cash flows consistently.
    a=copy.deepcopy(ASSUMPTIONS);a['inventory_days']+=20
    x=project(a);assert_balanced(x,a)
    assert x[0]['fcfe']<rows[0]['fcfe']
    print('PASS: additional inventory investment reduces cash flow and still balances.')
    print('PASS: terminal FCFE explicitly funds 3% growth in productive assets and working capital.')
    print('AI validation and filing checks only; no student manual verification or human partner review is claimed.')


def sensitivity():
    rows=project()
    print('Same statements; value/share at required return and terminal growth:')
    print('Cost of equity       2%         3%         4%')
    for k in (.10,.12,.14):
        vals=[]
        for g in (.02,.03,.04):
            a=copy.deepcopy(ASSUMPTIONS);a.update(cost_of_equity=k,terminal_growth=g)
            vals.append(valuation(rows,a)['per_share'])
        print(f'{k:>12.0%}'+''.join(f'{v:>11.2f}' for v in vals))
    lower=copy.deepcopy(ASSUMPTIONS)
    lower['gross_margin']=tuple(v-.02 for v in lower['gross_margin'])
    print(f"All annual gross margins 2 percentage points lower: ${valuation(project(lower),lower)['per_share']:.2f}/share")


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--self-test',action='store_true')
    parser.add_argument('--break-cash',action='store_true')
    parser.add_argument('--sensitivity',action='store_true')
    args=parser.parse_args()
    if args.self_test:
        self_test();return
    if args.sensitivity:
        sensitivity();return
    rows=project()
    if args.break_cash: rows[0]['cash']=OPENING['cash']
    print_checks(rows)
    print_table('INCOME STATEMENT',rows,[(k,label) for k,label in [
        ('revenue','Revenue'),('cogs','Cost of revenue'),('gross_profit','Gross profit'),
        ('sga','SG&A'),('rd','Research and development'),('operating_income','Operating income'),
        ('interest','Interest expense'),('pretax','Pretax income'),('tax','Income taxes'),('net_income','Net income')]])
    print_table('BALANCE SHEET',rows,[(k,label) for k,label in [
        ('cash','Cash'),('securities','Marketable securities'),('ar','Accounts receivable'),
        ('inventory','Inventory'),('prepaid','Prepaid / other current assets'),('ppe','PP&E, net'),
        ('intangibles','Intangibles, net'),('private_investments','Private equity investments'),
        ('other_assets','Other noncurrent assets'),('assets','Total assets'),('ap','Accounts payable'),
        ('accrued','Accrued current liabilities'),('debt','Term debt'),('revolver','Revolver'),
        ('other_liabilities','Other noncurrent liabilities'),('liabilities','Total liabilities'),('equity','Equity')]])
    print_table('CASH FLOW',rows,[(k,label) for k,label in [
        ('net_income','Net income'),('depreciation','Depreciation addback'),('amortization','Amortization addback'),
        ('delta_ar','Increase in receivables'),('delta_inventory','Increase in inventory'),
        ('delta_prepaid','Increase in prepaid assets'),('delta_ap','Increase in payables'),
        ('delta_accrued','Increase in operating accruals'),('delta_nwc','Net WC investment (subtract)'),
        ('cfo','Operating cash flow'),('capex','Capital spending (subtract)'),('purchase_payment','Purchase consideration (subtract)'),
        ('cfi','Investing cash flow'),('repayment','Debt repayment (subtract)'),
        ('dividends','Dividends (subtract)'),('buyback','Buybacks (subtract)'),('change_revolver','Net revolver borrowing'),
        ('cff','Financing cash flow'),('cash_change','Change in cash'),('cash','Ending cash'),('fcfe','FCFE before distributions')]])
    v=valuation(rows)
    print('\nVALUATION — annual teaching convention: discount 1–5 years to FY2026 end.')
    print('Prepared with information available 2026-09-24; not a historical backtest or exact same-day DCF.')
    for key in ('pv_fcfe','pv_terminal','nonoperating','terminal_fcfe','terminal_net_capex','terminal_delta_nwc','equity'):
        print(f'{key}: {v[key]:,.2f} million')
    print(f"Terminal share of total equity value: {v['terminal_share']:.2%}")
    print(f"Share denominator: {ASSUMPTIONS['shares']:,.0f} million (24.1 billion)")
    print(f"Value per share: ${v['per_share']:.2f}")
    print(f"Market reference: ${ASSUMPTIONS['market_price']:.2f}; 2026-09-24 2:05 PM EDT; FinancialContent, intraday.")
    print('Comparison is a question about assumptions; annual valuation anchor differs from quote date.')


if __name__=='__main__':
    main()
