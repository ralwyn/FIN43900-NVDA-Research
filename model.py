"""NVIDIA five-year pro-forma and FCFF DCF, USD millions and shares millions.
Valuation 2026-09-24. Latest reported BS 2026-07-26; intervening BS estimated.
No external packages, runtime downloads, credentials or hidden price updates.
"""
import copy
import datetime as dt
import math

AS_OF = dt.date(2026,9,24)
REPORTED_DATE = dt.date(2026,7,26)
ENDS = [dt.date(2027,1,31),dt.date(2028,1,30),dt.date(2029,1,28),dt.date(2030,1,27),dt.date(2031,1,26)]
SOURCE_Q2 = 'https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Announces-Financial-Results-for-Second-Quarter-Fiscal-2027/'
SOURCE_K = 'https://www.sec.gov/Archives/edgar/data/1045810/000104581026000021/nvda-20260125.htm'
OPENING = dict(cash=22443.,securities=34143.+42783.,ar=63059.,inventory=31575.,prepaid=3409.,
               ppe=14285.,intangibles=2998.,private_investments=51157.,other_assets=5390.+21125.+12159.+15746.,
               ap=15059.,accrued=26960.,debt=1000.+32366.,other_liabilities=4985.+10918.,equity=228984.)
H1 = dict(revenue=177837.,gross_profit=133299.,sga=2654.,rd=13375.,operating_income=117270.,
          net_income=118010.,tax=23400.,other_income=24140.,da=2124.,capex=4434.,cfo=74421.)
BASE = dict(growth=(.35,.25,.15,.08),gross_margin=(.74,.73,.72,.71,.70),
            sga_gp=(.025,.027,.029,.030,.030),rd_revenue=(.08,.09,.10,.11,.12),
            q3_revenue=108000.,q4_revenue=118800.,growth_shift=0.,margin_shift=0.,tax_rate=.17,
            ar_days=63059./(177837.*2)*365,inventory_days=31575./(44538.*2)*365,
            ap_days=15059./(44538.*2)*365,prepaid_revenue=3409./(177837.*2),
            accrued_revenue=26960./(177837.*2),depreciation_rate=.23,amortization_rate=.28,
            capex_revenue=.03,tangible_capex_share=.97,minimum_cash=5000.,
            shares=24285.,basic_shares=24100.,annual_dividend_per_share=1.,
            cost_of_equity=.12,cost_of_debt=.045,terminal_growth=.03,
            private_haircut=.25,market_price=224.58)
BS_ASSETS = ('cash','securities','ar','inventory','prepaid','ppe','intangibles','private_investments','other_assets')
BS_LIABS = ('ap','accrued','debt','other_liabilities')
FLOW_KEYS = ('revenue','gross_profit','cogs','sga','rd','operating_income','interest','pretax','tax','net_income',
             'depreciation','amortization','capex','tangible_capex','intangible_capex','delta_nwc','cfo','cfi','cff','dividends','cash_change','nopat','fcff')


def totals(r):
    r['assets'] = sum(r[k] for k in BS_ASSETS)
    r['liabilities'] = sum(r[k] for k in BS_LIABS)
    return r


def check_close(x,y,label):
    if not math.isfinite(x+y) or abs(x-y)>1e-6:
        raise ValueError(f'{label}: gap {x-y:,.6f}; valuation refused')


def validate_inputs(a):
    for key,v in a.items():
        vals = v if isinstance(v,(tuple,list)) else [v]
        if any(not isinstance(x,(int,float)) or not math.isfinite(x) for x in vals):
            raise ValueError('Non-finite/non-numeric input: '+key)
    if not -.10 <= a['growth_shift'] <= .10 or not -.05 <= a['margin_shift'] <= .05:
        raise ValueError('Growth and margin shifts outside the bounded stress domain.')
    if not .08 <= a['cost_of_equity'] <= .20 or not .01 <= a['cost_of_debt'] <= .10:
        raise ValueError('Required equity return must be 8–20%; borrowing cost 1–10%.')
    if not 0 <= a['terminal_growth'] <= .05 or not 0 <= a['tax_rate'] < 1:
        raise ValueError('Invalid terminal growth or tax rate.')
    if not 0 <= a['private_haircut'] <= 1 or a['shares'] <= 0 or a['basic_shares'] <= 0:
        raise ValueError('Invalid investment haircut or share count.')
    if any(not 0 < x+a['margin_shift'] < 1 for x in a['gross_margin']):
        raise ValueError('Gross margin must be between zero and one.')
    if a['capex_revenue'] < 0 or min(a['ar_days'],a['inventory_days'],a['ap_days']) < 0:
        raise ValueError('Negative investment or working-capital days.')


def check_statements(rows, opening, a):
    prior = totals(copy.deepcopy(opening))
    check_close(prior['assets'],prior['liabilities']+prior['equity'],'Opening balance sheet')
    for r in rows:
        if any(not math.isfinite(v) for v in r.values() if isinstance(v,(int,float))):
            raise ValueError('Non-finite statement output')
        t = totals(r.copy())
        check_close(t['assets'],t['liabilities']+r['equity'],f'FY{r["year"]} balance sheet')
        check_close(r['cash']-prior['cash'],r['cfo']+r['cfi']+r['cff'],'Cash rollforward')
        check_close(r['equity']-prior['equity'],r['net_income']-r['dividends'],'Equity rollforward')
        check_close(r['ppe']-prior['ppe'],r['tangible_capex']-r['depreciation'],'PP&E rollforward')
        check_close(r['intangibles']-prior['intangibles'],r['intangible_capex']-r['amortization'],'Intangible rollforward')
        check_close(r['net_income'],r['revenue']-r['cogs']-r['sga']-r['rd']-r['interest']-r['tax'],'Income statement')
        check_close(r['fcff'],r['cfo']-r['capex']+r['interest']*(1-a['tax_rate']),'FCFF/CFO reconciliation')
        check_close(r['debt'],prior['debt'],'Flat refinanced debt policy')
        if r['cash'] < a['minimum_cash']:
            raise ValueError('Cash below liquidity floor; no invented borrowing facility.')
        if min(r[k] for k in ('ar','inventory','ap','ppe','intangibles')) < 0:
            raise ValueError('Negative operating asset or payable.')
        prior = r


def project(a):
    validate_inputs(a)
    prior = totals(copy.deepcopy(OPENING))
    check_close(prior['assets'],320272.,'Reported total assets vs Q2 release')
    check_close(prior['liabilities'],91288.,'Reported total liabilities vs Q2 release')
    full_revenue = H1['revenue']+a['q3_revenue']+a['q4_revenue']
    rows=[]
    for i in range(5):
        period_years = (ENDS[0]-REPORTED_DATE).days/365. if i==0 else (ENDS[i]-ENDS[i-1]).days/365.
        if i==0:
            # Shock affects only unreported H2; actual H1 is locked.
            full_revenue = H1['revenue']+(a['q3_revenue']+a['q4_revenue'])*(1+a['growth_shift'])
            revenue = full_revenue-H1['revenue']
            gp = full_revenue*(a['gross_margin'][i]+a['margin_shift'])-H1['gross_profit']
            sga = full_revenue*(a['gross_margin'][i]+a['margin_shift'])*a['sga_gp'][i]-H1['sga']
            rd = full_revenue*a['rd_revenue'][i]-H1['rd']
        else:
            full_revenue *= 1+a['growth'][i-1]+a['growth_shift']
            revenue = full_revenue
            gp = revenue*(a['gross_margin'][i]+a['margin_shift'])
            sga = gp*a['sga_gp'][i]
            rd = revenue*a['rd_revenue'][i]
        r = dict(year=2027+i,period_years=period_years,revenue=revenue,annual_revenue=full_revenue,
                 gross_profit=gp,cogs=revenue-gp,sga=sga,rd=rd,operating_income=gp-sga-rd)
        r['interest'] = prior['debt']*a['cost_of_debt']*period_years
        r['pretax']=r['operating_income']-r['interest']
        r['tax']=max(r['pretax'],0)*a['tax_rate']
        r['net_income']=r['pretax']-r['tax']
        r['depreciation']=prior['ppe']*a['depreciation_rate']*period_years
        r['amortization']=prior['intangibles']*a['amortization_rate']*period_years
        r['capex']=revenue*a['capex_revenue']
        r['tangible_capex']=r['capex']*a['tangible_capex_share']
        r['intangible_capex']=r['capex']-r['tangible_capex']
        r['ppe']=prior['ppe']+r['tangible_capex']-r['depreciation']
        r['intangibles']=prior['intangibles']+r['intangible_capex']-r['amortization']
        # Annual-intensity WC; first forecast year incorporates known H1 actuals.
        annual_cogs=full_revenue*(1-a['gross_margin'][i]-a['margin_shift'])
        r['ar']=full_revenue*a['ar_days']/365
        r['inventory']=annual_cogs*a['inventory_days']/365
        r['ap']=annual_cogs*a['ap_days']/365
        r['prepaid']=full_revenue*a['prepaid_revenue']
        r['accrued']=full_revenue*a['accrued_revenue']
        for key in ('debt','securities','private_investments','other_assets','other_liabilities'):
            r[key]=prior[key]
        r['delta_nwc']=sum(r[k]-prior[k] for k in ('ar','inventory','prepaid'))-sum(r[k]-prior[k] for k in ('ap','accrued'))
        r['cfo']=r['net_income']+r['depreciation']+r['amortization']-r['delta_nwc']
        r['cfi']=-r['capex']
        r['dividends']=a['annual_dividend_per_share']*a['basic_shares']*period_years
        r['cff']=-r['dividends']
        r['cash_change']=r['cfo']+r['cfi']+r['cff']
        r['cash']=prior['cash']+r['cash_change']
        r['equity']=prior['equity']+r['net_income']-r['dividends']
        r['nopat']=r['operating_income']*(1-a['tax_rate'])
        r['fcff']=r['nopat']+r['depreciation']+r['amortization']-r['capex']-r['delta_nwc']
        totals(r)
        rows.append(r)
        prior=r
    check_statements(rows,OPENING,a)
    return rows


def value(a=None, broken=False):
    a=copy.deepcopy(BASE if a is None else a)
    rows=project(a)
    # Straight-line operating roll from last reported quarter to valuation date.
    elapsed=(AS_OF-REPORTED_DATE).days/(ENDS[0]-REPORTED_DATE).days
    estimated={key:OPENING[key]+elapsed*(rows[0][key]-OPENING[key]) for key in BS_ASSETS+BS_LIABS+('equity',)}
    totals(estimated)
    future=copy.deepcopy(rows)
    for key in FLOW_KEYS:
        future[0][key] *= 1-elapsed
    future[0]['period_years'] *= 1-elapsed
    if broken:
        future[0]['cash']+=1
    check_statements(future,estimated,a)
    market_equity=a['market_price']*a['basic_shares']
    debt=estimated['debt']
    debt_weight=debt/(debt+market_equity)
    wacc=a['cost_of_equity']*(1-debt_weight)+a['cost_of_debt']*(1-a['tax_rate'])*debt_weight
    g=a['terminal_growth']
    if wacc<=g:
        raise ValueError('WACC must exceed terminal growth.')
    times=[(end-AS_OF).days/365. for end in ENDS]
    last=rows[-1]
    terminal_revenue=last['annual_revenue']*(1+g)
    terminal_ebit=terminal_revenue*((a['gross_margin'][-1]+a['margin_shift'])*(1-a['sga_gp'][-1])-a['rd_revenue'][-1])
    nwc=last['ar']+last['inventory']+last['prepaid']-last['ap']-last['accrued']
    terminal_net_investment=g*(last['ppe']+last['intangibles']+nwc)
    terminal_fcff=terminal_ebit*(1-a['tax_rate'])-terminal_net_investment
    if terminal_fcff<=0:
        raise ValueError('Nonpositive terminal FCFF: revise terminal economics.')
    pv_flows=sum(r['fcff']/(1+wacc)**t for r,t in zip(future,times))
    pv_terminal=terminal_fcff/(wacc-g)/(1+wacc)**times[-1]
    enterprise=pv_flows+pv_terminal
    bridge=dict(excess_cash=max(0,estimated['cash']-a['minimum_cash']),marketable_securities=estimated['securities'],
                private_investments_after_haircut=estimated['private_investments']*(1-a['private_haircut']),debt=-debt,
                preferred_stock=0.,noncontrolling_interest=0.)
    equity=enterprise+sum(bridge.values())
    return dict(status='Dated scenario valuation with estimated interim balances; review assumptions and limits',
                valuation_date=AS_OF.isoformat(),discount_anchor=AS_OF.isoformat(),information_boundary='2026-09-24; sources rechecked 2026-10-19',
                currency_and_scale='USD millions; shares millions; per-share USD',committee_action='WATCH / DEFER',
                assumptions=a,reported_opening=totals(OPENING.copy()),estimated_valuation_balance=estimated,
                annual_forecast_periods=rows,statements=future,first_period='Remaining FY2027 stub; FY2028–31 are annual periods',
                wacc=wacc,wacc_components=dict(equity_value_weight_base=market_equity,debt=debt,debt_weight=debt_weight,
                cost_of_equity=a['cost_of_equity'],cost_of_debt=a['cost_of_debt'],tax_rate=a['tax_rate']),
                discount_times=times,terminal_net_investment=terminal_net_investment,terminal_fcff=terminal_fcff,
                pv_fcff=pv_flows,pv_terminal=pv_terminal,enterprise_value=enterprise,terminal_value_share_of_ev=pv_terminal/enterprise,
                bridge=bridge,equity_value=equity,per_share=equity/a['shares'])


def assumptions(growth_shift=0,margin_shift=0,wacc=.12,terminal_growth=.03):
    # Public compatibility argument 'wacc' controls required equity return; actual WACC is derived.
    a=copy.deepcopy(BASE)
    a.update(growth_shift=growth_shift,margin_shift=margin_shift,cost_of_equity=wacc,terminal_growth=terminal_growth)
    return a
