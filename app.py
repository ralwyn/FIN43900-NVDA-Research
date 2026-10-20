"""Local pro-forma workbench: python3 app.py, then http://127.0.0.1:8439.
No installation or credentials. Controls rerun the Python accounting engine.
"""
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs, urlparse
import html
import json
from analysis import assumptions, value, report


def render(query):
    q = parse_qs(query)
    defaults = {'growth':0, 'margin':0, 'wacc':12, 'terminal':3}
    controls = {key:float(q.get(key,[default])[0]) for key,default in defaults.items()}
    warning = ''
    try:
        a = assumptions(controls['growth']/100,controls['margin']/100,controls['wacc']/100,controls['terminal']/100)
        result = value(a, broken=q.get('break_cash') == ['1'])
        base = value()
        status = f'PASS — all five forecast periods articulate. Value ${result["per_share"]:.2f}/share; change from restored base ${result["per_share"]-base["per_share"]:+.2f}. Derived WACC {result["wacc"]:.2%}.'
        tone = 'pass'
    except ValueError as e:
        result = None
        status, tone = 'VALUATION BLOCKED: '+str(e), 'fail'
    fields = []
    for key,label,lo,hi,step in [('growth','Revenue-growth shift (percentage points)',-10,10,.5),('margin','Gross-margin shift (percentage points)',-5,5,.5),('wacc','Required equity return (%)',8,20,.5),('terminal','Terminal growth (%)',0,5,.5)]:
        fields.append(f'<label>{label}<input name="{key}" type="number" min="{lo}" max="{hi}" step="{step}" value="{controls[key]}"></label>')
    body = f'<p class="{tone}" role="status">{html.escape(status)}</p>'
    if result:
        rows = result['statements']
        body += '<h2>Enterprise-to-equity bridge · USD millions</h2><table><tr><th>Component</th><th>Value</th></tr>'
        bridge = {'Operating enterprise value':result['enterprise_value'], **result['bridge'], 'Common equity':result['equity_value'], 'Diluted share proxy (millions)':result['assumptions']['shares']}
        body += ''.join(f'<tr><td>{html.escape(k)}</td><td>{v:,.2f}</td></tr>' for k,v in bridge.items()) + '</table>'
        body += f'<p>Terminal value: {result["terminal_value_share_of_ev"]:.1%} of EV. Shares: Q2 FY2027 diluted weighted-average proxy (24,285m), not a forward dilution forecast. The first column is the remaining FY2027 stub; later columns are annual. All flows before September 24 are excluded from DCF.</p>'
        body += '<h2>Linked statements · USD millions</h2><table><tr><th>Line</th>'+''.join(f'<th>FY{r["year"]}E</th>' for r in rows)+'</tr>'
        for key in ['revenue','gross_profit','sga','rd','operating_income','interest','tax','net_income','cash','securities','ar','inventory','prepaid','ppe','intangibles','private_investments','other_assets','assets','ap','accrued','debt','other_liabilities','liabilities','equity','cfo','cfi','cff','cash_change','nopat','capex','delta_nwc','fcff']:
            body += f'<tr><td>{key.replace("_"," ")}</td>'+''.join(f'<td>{r[key]:,.1f}</td>' for r in rows)+'</tr>'
        body += '</table><details><summary>All inputs and model outputs</summary><pre>'+html.escape(json.dumps(result,indent=2))+'</pre></details>'
        pack=report()
        body+='<h2>Frozen causal cases</h2><table><tr><th>Case</th><th>USD/share</th><th>WACC</th></tr>'
        for n,x in pack['cases'].items():body+=f'<tr><td>{html.escape(n)}</td><td>{x["per_share"]:.2f}</td><td>{x["wacc"]:.2%}</td></tr>'
        body+='</table><h2>WACC / terminal-growth sensitivity</h2><table><tr><th>WACC</th><th>g 2%</th><th>g 3%</th><th>g 4%</th></tr>'
        for w,gs in pack['wacc_growth_sensitivity'].items():body+='<tr><td>'+w+'</td>'+''.join(f'<td>{v:.2f}</td>' for v in gs.values())+'</tr>'
        body+='</table><h2>Market-implied growth test</h2><pre>'+html.escape(json.dumps(pack['reverse_dcf'],indent=2))+'</pre>'
    return '''<!doctype html><html lang="en"><meta charset="utf-8"><title>NVIDIA Pro-Forma Workbench</title>
<style>body{font:16px system-ui;max-width:1200px;margin:32px auto;padding:20px;color:#17233b;background:#f5f7fa}form{display:flex;gap:16px;flex-wrap:wrap;background:white;padding:20px;border-radius:12px}label{display:grid;gap:8px}input{padding:10px;font-size:16px;width:180px}button,a{padding:10px}table{border-collapse:collapse;background:white;width:100%;font-size:14px}td,th{border-bottom:1px solid #dde2ea;padding:8px;text-align:right}td:first-child,th:first-child{text-align:left}.pass{background:#d7efdf;padding:18px}.fail{background:#ffdddd;padding:18px}pre{overflow:auto}aside{border-left:5px solid #c98300;padding:15px;background:#fff3d1}</style>
<h1>NVIDIA pro-forma workbench</h1><p>FIN439 Project 1 · committee action proposed for review: WATCH / DEFER</p>
<aside>Valuation date: September 24, 2026 close ($224.58). Latest reported balance sheet: July 26. September balances are estimated by a disclosed straight-line operating roll. Future cash flows start September 24. This is a historical dated scenario analysis, not an October 19 price target. Independent validation and AI-use details are in the separate validation record.</aside>
<p>Growth bounds ±10 points and margin bounds ±5 points are exploratory stress limits. Required equity return and debt cost are judgments; WACC is calculated from equity/debt weights and the tax shield. Base required equity return 12%, debt cost 4.5%, tax 17%.</p>
<form>'''+''.join(fields)+'''<label>Demonstrate accounting guard<input name="break_cash" type="checkbox" value="1">Inject $1m cash error</label><button type="submit">Recalculate</button><a href="/">Restore base</a></form>'''+body+'</html>'


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if urlparse(self.path).path != '/':
            self.send_error(404)
            return
        try:
            page = render(urlparse(self.path).query)
        except (ValueError, OverflowError) as error:
            page = '<h1>Invalid input — valuation blocked</h1><p>'+html.escape(str(error))+'</p><a href="/">Restore base</a>'
        data = page.encode()
        self.send_response(200)
        self.send_header('Content-Type','text/html; charset=utf-8')
        self.send_header('Content-Length',str(len(data)))
        self.end_headers()
        self.wfile.write(data)


if __name__ == '__main__':
    print('Open http://127.0.0.1:8439 — Ctrl+C to stop', flush=True)
    HTTPServer(('127.0.0.1',8439), Handler).serve_forever()
