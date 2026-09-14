"""Create a self-contained immutable full ZIP and SHA-256 manifests."""
from pathlib import Path
import hashlib,json,zipfile
ROOT=Path(__file__).resolve().parents[1]
state=json.loads((ROOT/'editorial/progress.json').read_text(encoding='utf-8'))
out=ROOT.parent/'backups'
out.mkdir(exist_ok=True)
name=f"SQFT_v{state['version']}_{state['last_revision_date']}_through_ch{max(state['completed_chapters']):02d}_FULL.zip"
target=out/name
if target.exists():
    raise SystemExit('This immutable snapshot already exists. Use a new revision version, never overwrite it.')
def sha(p):
    h=hashlib.sha256()
    with p.open('rb') as f:
        for chunk in iter(lambda:f.read(1024*1024),b''):h.update(chunk)
    return h.hexdigest()
manifest={p.relative_to(ROOT).as_posix():{'bytes':p.stat().st_size,'sha256':sha(p)}
          for p in sorted(ROOT.rglob('*')) if p.is_file() and p.name!='SHA256_MANIFEST.json' and '__pycache__' not in p.parts}
(ROOT/'SHA256_MANIFEST.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf-8')
with zipfile.ZipFile(target,'x',compression=zipfile.ZIP_DEFLATED,compresslevel=6) as z:
    for rel in manifest:z.write(ROOT/rel,arcname=f'{ROOT.name}/{rel}')
    z.write(ROOT/'SHA256_MANIFEST.json',arcname=f'{ROOT.name}/SHA256_MANIFEST.json')
with zipfile.ZipFile(target) as z:
    assert z.testzip() is None,'ZIP integrity failed'
    assert len(z.namelist())==len(manifest)+1
digest=sha(target)
target.with_suffix('.zip.sha256').write_text(f'{digest}  {target.name}\n',encoding='utf-8')
print(json.dumps({'archive':str(target),'bytes':target.stat().st_size,'files':len(manifest)+1,'sha256':digest,'crc_verified':True}))
