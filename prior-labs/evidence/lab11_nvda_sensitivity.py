"""Lab 11: rerun the existing NVIDIA model one operating input at a time.
Run: python3 lab11_nvda_sensitivity.py
Outputs are written alongside this script. Standard library only.
Ranges are AI-proposed judgments, editable in DRIVERS; not company guidance.
"""
import copy
import hashlib
import io
import json
import math
from contextlib import redirect_stdout
from datetime import datetime, timezone
from pathlib import Path
import nvda_proforma as model

HERE = Path(__file__).resolve().parent
DRIVERS = {'growth': 0.05, 'gross_margin': 0.02}
NAMES = {'growth': 'Revenue growth', 'gross_margin': 'Gross margin'}
METRICS = ('operating_income', 'fcfe', 'per_share')


def run_case(name, inputs, original, driver=None):
    changed = [k for k in original if inputs[k] != original[k]]
    assert changed == ([] if driver is None else [driver]), changed
    record = dict(name=name, inputs=copy.deepcopy(inputs), changed_keys=changed,
                  accounting_valid=False, valuation_valid=False)
    log = io.StringIO()
    try:
        rows = model.project(inputs)
        record['statements'] = rows
        with redirect_stdout(log):
            model.print_checks(rows, inputs)
        record['accounting_valid'] = True
        record['outputs'] = dict(operating_income=rows[-1]['operating_income'],
                                 fcfe=rows[-1]['fcfe'], per_share=None)
        try:
            value = model.valuation(rows, inputs)
            record['valuation'] = value
            record['outputs']['per_share'] = value['per_share']
            record['valuation_valid'] = True
        except ValueError as exc:
            record['valuation_error'] = str(exc)
    except (ValueError, OverflowError, ZeroDivisionError) as exc:
        record['accounting_error'] = str(exc)
    record['checks'] = log.getvalue()
    return record


def main():
    base = copy.deepcopy(model.ASSUMPTIONS)
    initial = run_case('Base before', copy.deepcopy(base), base)
    assert initial['accounting_valid'], initial
    records = [initial]
    spans = {}
    for key, shift in DRIVERS.items():
        group = []
        for label, offset in [('Lower', -shift), ('Base', 0), ('Higher', shift)]:
            inputs = copy.deepcopy(base)
            inputs[key] = tuple(x + offset for x in base[key])
            record = run_case(f'{NAMES[key]} — {label}', inputs, base,
                              key if offset else None)
            record.update(driver=key, level=label)
            if record['accounting_valid']:
                record['delta'] = {m: (record['outputs'][m]-initial['outputs'][m]
                                      if record['outputs'][m] is not None and initial['outputs'][m] is not None
                                      else None) for m in METRICS}
            records.append(record)
            group.append(record)
        spans[key] = {}
        for metric in METRICS:
            valid = [r['outputs'][metric] for r in group if r['accounting_valid']
                     and r['outputs'][metric] is not None]
            spans[key][metric] = dict(span=max(valid)-min(valid) if len(valid)>1 else None,
                                     valid_runs=len(valid), complete=len(valid)==3)
    restored = run_case('Base restored', copy.deepcopy(base), base)
    assert base == model.ASSUMPTIONS == initial['inputs'] == restored['inputs']
    assert restored['accounting_valid']
    for before, after in zip(initial['statements'], restored['statements']):
        for key in before:
            assert math.isclose(before[key], after[key], rel_tol=0, abs_tol=1e-6), key
    assert initial.get('valuation') == restored.get('valuation')
    records.append(restored)
    payload = dict(created_utc=datetime.now(timezone.utc).isoformat(),
                   model_sha256=hashlib.sha256((HERE/'nvda_proforma.py').read_bytes()).hexdigest(),
                   ranges=DRIVERS, restored_base='PASS; all statement fields within 0.000001 USD million; inputs and valuation identical',
                   spans=spans, runs=records)
    (HERE/'lab11-nvda-details.json').write_text(json.dumps(payload, indent=2, allow_nan=False)+'\n')
    lines = ['NVIDIA LAB 11 — ONE-AT-A-TIME SENSITIVITY',
             'USD millions, except USD/share. Final year: FY2031. Cash flow: FCFE.',
             'Judgment ranges: growth +/-5 pp; gross margin +/-2 pp; every FY2027–FY2031.',
             'Ranges are AI-proposed and require student review; no probability is implied.',
             'Original Lab 10 inputs and valuation convention retained; no refreshed market data.', '']
    for r in records:
        lines += [r['name'], 'Changed independent keys: '+str(r['changed_keys']),
                  'Growth FY2027–31 (%): '+', '.join(f'{x*100:.6f}' for x in r['inputs']['growth']),
                  'Gross margin FY2027–31 (%): '+', '.join(f'{x*100:.6f}' for x in r['inputs']['gross_margin']),
                  r['checks']]
        if not r['accounting_valid']:
            lines.append('INVALID — excluded from ranking: '+r['accounting_error'])
            continue
        for m in METRICS:
            v = r['outputs'][m]
            delta = r.get('delta', {}).get(m)
            lines.append(f'{m}: {v:,.6f}' if v is not None else f'{m}: unavailable')
            if delta is not None:
                lines.append(f'  signed change from base: {delta:+,.6f}')
        if not r['valuation_valid']:
            lines.append('Valuation unavailable: '+r['valuation_error'])
        lines.append('')
    lines += ['SPANS (maximum minus minimum; invalid results excluded)', json.dumps(spans, indent=2),
              'RESTORED BASE: '+payload['restored_base']]
    output = '\n'.join(lines)+'\n'
    (HERE/'lab11-nvda-output.txt').write_text(output)
    print(output)


if __name__ == '__main__':
    main()
