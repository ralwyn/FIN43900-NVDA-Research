"""Supplement prepared Oct 1, 2026, not a recovered Week 3 result.
Solve a uniform percentage-point shift in FY2027–31 growth to match the saved
Sep 24 price of $224.20, preserving all other Lab 10 independent assumptions.
Standard library only. Run: python3 reverse_dcf.py
"""
import copy
import json
import math
import sys
from pathlib import Path
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE/'evidence'))
import nvda_proforma as m
base=copy.deepcopy(m.ASSUMPTIONS)
def evaluate(shift):
    a=copy.deepcopy(base)
    a['growth']=tuple(v+shift for v in base['growth'])
    rows=m.project(a)
    m.assert_balanced(rows,a)
    val=m.valuation(rows,a)
    return a,rows,val
if __name__=='__main__':
    target=base['market_price']
    lo,hi=0.0,0.5
    assert evaluate(lo)[2]['per_share']<=target<=evaluate(hi)[2]['per_share']
    for _ in range(80):
        mid=(lo+hi)/2
        if evaluate(mid)[2]['per_share']<target:lo=mid
        else:hi=mid
    shift=(lo+hi)/2
    a,rows,v=evaluate(shift)
    assert math.isclose(v['per_share'],target,rel_tol=0,abs_tol=1e-8)
    assert [k for k in a if a[k]!=base[k]]==['growth']
    restored=evaluate(0)
    assert m.ASSUMPTIONS==base
    assert restored[1]==m.project(copy.deepcopy(base))
    out={'prepared':'2026-10-01','status':'New Lab 12 preparation supplement; not original Week 3 work',
         'target_price':target,'price_date':'2026-09-24 14:05 EDT, saved intraday reference',
         'valuation_basis':'Original annual convention: discount FY2027–31 cash flows to FY2026 end; not current-date valuation',
         'currency':'USD; statements in millions; shares in millions',
         'shift_percentage_points':shift*100,'base_growth_percent':[x*100 for x in base['growth']],
         'implied_growth_percent':[x*100 for x in a['growth']],
         'fixed_assumptions':{k:v for k,v in base.items() if k!='growth'},
         'result_per_share':v['per_share'],'FY2031_revenue_millions':rows[-1]['revenue'],
         'FY2031_FCFE_millions':rows[-1]['fcfe'],'checks':'PASS: all five years; target within $0.00000001/share; base restored',
         'statements':rows,'valuation':v}
    (HERE/'reverse-dcf-results.json').write_text(json.dumps(out,indent=2)+'\n')
    text='\n'.join(['NEW REVERSE-DCF PREPARATION SUPPLEMENT — October 1, 2026',
         'Not a recovered Week 3 result. No new market quote used.',
         'Saved September 24 reference: $224.20/share.',
         f'Uniform growth shift: +{shift*100:.6f} percentage points in each FY2027–FY2031.',
         'Implied annual growth (%): '+', '.join(f'{x*100:.6f}' for x in a['growth']),
         f'Recomputed value: ${v["per_share"]:.8f}/share.',
         'Held fixed: every other independent Lab 10 input, including gross-margin path, taxes, investment ratios, 12% cost of equity, 3% terminal growth, and 24,100m shares.',
         f'FY2031 revenue: ${rows[-1]["revenue"]:,.2f}m; FCFE: ${rows[-1]["fcfe"]:,.2f}m.',
         out['checks'],
         'Interpretation: one conditional path that matches the reference price; not the unique expectations embedded in the stock.',
         'Limitation: annual discounting anchor and saved quote date differ. FY2027 shift changes full-year revenue despite some actual months being known.'])+'\n'
    (HERE/'reverse-dcf-output.txt').write_text(text)
    print(text)
