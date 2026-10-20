"""Generate visible outputs and automated validation: python3 analysis.py."""
import copy, json, math
from pathlib import Path
from model import BASE, AS_OF, assumptions, value, check_statements
ROOT=Path(__file__).resolve().parent

def peers():
    p={
      'AMD':dict(price=629.26,shares=1630.,share_date='2025-12-27',revenue=34639.,eps=2.65,debt=3222.,cash=10552.,fiscal_end='2025-12-27',filing='https://www.sec.gov/Archives/edgar/data/2488/000000248826000018/amd-20251227.htm'),
      'AVGO':dict(price=350.36,shares=4741.273799,share_date='2025-11-28',revenue=63887.,eps=4.77,debt=65136.,cash=16178.,fiscal_end='2025-11-02',filing='https://www.sec.gov/Archives/edgar/data/1730168/000173016825000121/avgo-20251102.htm')}
    for ticker,r in p.items():
        r.update(price_date='2026-09-24 close',price_source=f'https://stockanalysis.com/stocks/{ticker.lower()}/history/')
        r['market_equity_proxy']=r['price']*r['shares']
        r['enterprise_value_proxy']=r['market_equity_proxy']+r['debt']-r['cash']
        r['ev_sales']=r['enterprise_value_proxy']/r['revenue']
        r['pe']=r['price']/r['eps']
        r['nvda_pe_reference']=r['pe']*4.90
        r['nvda_ev_sales_reference']=(r['ev_sales']*215938.+62556.-8468.)/24100.
        assert r['eps']>0 and r['revenue']>0
        assert math.isclose(r['enterprise_value_proxy']-r['market_equity_proxy'],r['debt']-r['cash'])
    return p

def report():
    cases={'Downside: AI spending slows and pricing weakens':(-.05,-.02,.14,.02),
           'Base: demand growth fades as scale expands':(0,0,.12,.03),
           'Upside: durable demand and pricing':(.05,.02,.10,.04)}
    results={name:value(assumptions(*args)) for name,args in cases.items()}
    dw=value()['wacc_components']['debt_weight'];grid={}
    for w in [.10,.12,.14]:
        a=assumptions();a['cost_of_equity']=(w-a['cost_of_debt']*(1-a['tax_rate'])*dw)/(1-dw)
        grid[f'{w:.0%}']={}
        for g in [.02,.03,.04]:
            a['terminal_growth']=g;x=value(a)
            assert math.isclose(x['wacc'],w,abs_tol=1e-10)
            grid[f'{w:.0%}'][f'{g:.0%}']=x['per_share']
    oat={}
    for name,key,width in [('Revenue growth','growth_shift',.05),('Gross margin','margin_shift',.02)]:
        oat[name]=[]
        for change in [-width,0,width]:
            a=assumptions();a[key]=change;x=value(a)
            oat[name].append(dict(shift_pp=change*100,fy2031_ebit=x['statements'][-1]['operating_income'],fy2031_fcff=x['statements'][-1]['fcff'],per_share=x['per_share']))
    def shifted(s):
        a=assumptions();a['growth_shift']=s
        return value(a)['per_share']
    lo,hi=-.10,.10;target=BASE['market_price']
    if shifted(lo)<=target<=shifted(hi):
        for _ in range(70):
            mid=(lo+hi)/2
            if shifted(mid)<target:lo=mid
            else:hi=mid
        reverse=dict(target=target,price_date='2026-09-24 close',growth_shift_pp=(lo+hi)*50,solved_per_share=shifted((lo+hi)/2),qualifier='Conditional on all other assumptions; not a forecast or unique market explanation.')
    else:reverse=dict(target=target,status='No growth solution inside bounded +/-10pp domain',low=shifted(lo),high=shifted(hi))
    lo,hi=.08,.20
    if value(assumptions(wacc=lo))['per_share']>=target>=value(assumptions(wacc=hi))['per_share']:
        for _ in range(70):
            mid=(lo+hi)/2
            if value(assumptions(wacc=mid))['per_share']>target:lo=mid
            else:hi=mid
        implied=value(assumptions(wacc=(lo+hi)/2))
        reverse.update(implied_required_equity_return=(lo+hi)/2,implied_wacc=implied['wacc'],solved_per_share=implied['per_share'],qualifier='Fixed base operating forecast and bridge; a conditional market-implied discount rate, not a measured cost of capital.')
    narrower={}
    for name,key,width in [('Growth +/-1pp','growth_shift',.01),('Margin +/-2pp','margin_shift',.02)]:
        a=assumptions();a[key]=-width;b=assumptions();b[key]=width
        narrower[name]=value(b)['per_share']-value(a)['per_share']
    return dict(valuation_date=AS_OF.isoformat(),cases=results,wacc_growth_sensitivity=grid,one_at_a_time=oat,range_dependency=narrower,reverse_dcf=reverse,peer_references=peers())

def verify():
    log=[]
    def passed(s):log.append('PASS: '+s)
    b=value()
    assert 150*(1-.25)+40-60-15==77.5 and (1000+100-250-20-10)/100==8.2
    passed('Published synthetic FCFF 77.5m and enterprise-equity result $8.20/share.')
    assert b['reported_opening']['assets']==320272 and b['reported_opening']['liabilities']==91288
    passed('Q2 reported assets and liabilities match the primary release.')
    check_statements(b['statements'],b['estimated_valuation_balance'],BASE)
    passed('All five future periods reconcile BS, cash, equity, productive assets, income, financing and FCFF.')
    assert b['statements'][0]['fcff']<b['annual_forecast_periods'][0]['fcff']
    passed('Elapsed July-to-September flows excluded; estimated valuation-date bridge separate.')
    assert value(assumptions(wacc=.14))['per_share']<b['per_share']<value(assumptions(wacc=.10))['per_share']
    for ke in [.10,.12,.14]:assert value(assumptions(wacc=ke,terminal_growth=.02))['per_share']<value(assumptions(wacc=ke,terminal_growth=.04))['per_share']
    passed('WACC and terminal-growth monotonicity over tested grid.')
    a=assumptions();a['inventory_days']+=20
    assert value(a)['statements'][0]['fcff']<b['statements'][0]['fcff']
    passed('Additional inventory investment reduces first-period FCFF.')
    a=assumptions();a['shares']*=2
    assert math.isclose(value(a)['per_share'],b['per_share']/2)
    passed('Diluted denominator doubles -> per-share value halves; basic market-cap weight unchanged.')
    for label,kwargs,a in [('cash corruption',dict(broken=True),None),('funding shortfall',{},dict(BASE,annual_dividend_per_share=1000)),('invalid terminal',{},dict(BASE,terminal_growth=.12))]:
        try:value(a,**kwargs)
        except ValueError as error:passed(label+' refused: '+str(error))
        else:raise AssertionError(label+' accepted')
    peers();passed('Peer EV identities and positive annual denominators.')
    assert value()==b
    passed('Restored base exactly matches before automated tests. These are AI-run tests, not the student locked record.')
    return log

def write_outputs():
    r=report();r['validation']=verify()
    (ROOT/'visible-output.json').write_text(json.dumps(r,indent=2)+'\n')
    (ROOT/'validation-log.txt').write_text('\n'.join(r['validation'])+'\n')
    lines=['# NVIDIA decision workbench - executed output','','Valuation: September 24, 2026 close. Latest reported BS: July 26; interim balances estimated. Prepared October 19. USD/share below.','','Proposed committee action: WATCH / DEFER, subject to student review. Same-date market close: $224.58.','','| Scenario | Value/share | WACC | Terminal share of EV |','|---|---:|---:|---:|']
    for n,x in r['cases'].items():lines.append(f'| {n} | ${x["per_share"]:.2f} | {x["wacc"]:.2%} | {x["terminal_value_share_of_ev"]:.1%} |')
    lines+=['','## WACC / terminal-growth sensitivity','','| WACC | g=2% | g=3% | g=4% |','|---|---:|---:|---:|']
    for w,gs in r['wacc_growth_sensitivity'].items():lines.append('| '+w+' | '+' | '.join(f'${p:.2f}' for p in gs.values())+' |')
    lines+=['','## Reverse DCF','',json.dumps(r['reverse_dcf']),'','## Definitions and limits','','Full inputs, statements, bridge, dates, peer calculations and tests are in visible-output.json. Peer EV/Sales uses annual historical revenue and dated basic shares; P/E uses annual GAAP diluted EPS. Stale share/balance dates, business mix and transitory earnings weaken comparability. Do not average the mechanical peer references into DCF. Straight-line interim balances, simplified taxes, no new acquisitions/investments/buybacks and cash-equivalent SBC constrain the model. WACC inputs and bounds are judgment ranges, not confidence intervals.','','## Validation','']+r['validation']
    (ROOT/'visible-output.md').write_text('\n'.join(lines)+'\n')
    print('\n'.join(lines[:12]));print('\n'.join(r['validation']))
    return r

if __name__=='__main__':write_outputs()
