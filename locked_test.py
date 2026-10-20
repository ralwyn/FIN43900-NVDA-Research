"""Student-operated two-stage record. Do not run with AI assistance on prediction/execution.
python3 locked_test.py prepare
python3 locked_test.py run
"""
import datetime as dt
import hashlib
import json
from pathlib import Path
import shutil
import sys

ROOT=Path(__file__).resolve().parent
RECORD=ROOT/'docs/locked-input'

def digest(path):return hashlib.sha256(path.read_bytes()).hexdigest()

def prepare():
    if RECORD.exists():raise SystemExit('A record already exists. Preserve it; do not overwrite history.')
    print('Fresh test: private-investment valuation haircut from 25% to 40%; all other inputs fixed.')
    print('Do not ask AI to write or check this prediction. No valuation is executed in this stage.')
    prediction=input('Your expected direction and finance reason: ').strip()
    size=input('Your rough expected size, with units and reasoning: ').strip()
    effect=input('Your expected committee-decision effect and why: ').strip()
    if not all([prediction,size,effect]):raise SystemExit('All three personal fields are required.')
    RECORD.mkdir(parents=True)
    for name in ['model.py','locked_test.py']:
        shutil.copy2(ROOT/name,RECORD/name)
    record=dict(timestamp_utc=dt.datetime.now(dt.timezone.utc).isoformat(),input='private_haircut',old=.25,new=.40,
                units='fraction of private-investment carrying value deducted (25% -> 40%)',
                student_prediction=prediction,student_size_prediction=size,student_decision_prediction=effect,
                snapshot_hashes={n:digest(RECORD/n) for n in ['model.py','locked_test.py']},
                provenance='Student entered prediction in local terminal; execution has not occurred. Prepared after earlier AI work; not a reconstructed Lab 11 record.')
    file=RECORD/'precommit.json';file.write_text(json.dumps(record,indent=2)+'\n')
    for path in RECORD.iterdir():path.chmod(0o444)
    print('Precommit saved:',file)
    print('SHA256:',digest(file))
    print('Preserve this hash and timestamp. With AI closed, now run: python3 locked_test.py run')

def run():
    path=RECORD/'precommit.json'
    if not path.exists():raise SystemExit('Prepare and preserve your prediction before running.')
    if (RECORD/'result.json').exists():raise SystemExit('Result already exists; preserve the first run.')
    p=json.loads(path.read_text())
    for n,h in p['snapshot_hashes'].items():
        if digest(ROOT/n)!=h or digest(RECORD/n)!=h:raise SystemExit('Source changed after precommit; do not run a mismatched test.')
    from model import BASE,value
    before=value();a=dict(BASE);a[p['input']]=p['new'];after=value(a)
    result=dict(executed_utc=dt.datetime.now(dt.timezone.utc).isoformat(),precommit_sha256=digest(path),
                before=before,after=after,delta_per_share=after['per_share']-before['per_share'])
    print('BEFORE $/share:',before['per_share'],'AFTER:',after['per_share'],'DELTA:',result['delta_per_share'])
    result['student_actual_decision_effect']=input('Actual decision effect, in your own words: ').strip()
    result['student_reconciliation']=input('Compare with prediction; diagnose differences or explain no action change: ').strip()
    out=RECORD/'result.json';out.write_text(json.dumps(result,indent=2)+'\n');out.chmod(0o444)
    print('Preserved complete before/after outputs:',out)
    print('This records a fresh test today, not an earlier lab event. Disclose timing honestly.')

if __name__=='__main__':
    if len(sys.argv)!=2 or sys.argv[1] not in ['prepare','run']:raise SystemExit(__doc__)
    {'prepare':prepare,'run':run}[sys.argv[1]]()
