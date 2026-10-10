"""Build UFI's custom repository response from committed original plugin blobs."""
import hashlib
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def git(*args):
    return subprocess.check_output(['git', '-C', str(ROOT), *args])

commit = git('rev-parse', 'HEAD').decode().strip()
names = git('ls-tree', '-r', '--name-only', '-z', commit, '--', 'ufi-tools-plugins').decode().strip('\0').split('\0')
items = []
for path in sorted(names):
    name = path.split('/', 1)[1]
    # UFI interpolates names into HTML and inline onclick handlers.
    if any(c in name for c in "'\"<>\\\r\n"):
        raise ValueError(f'Filename is not safe for the upstream renderer: {name}')
    data = git('show', f'{commit}:{path}')
    modified = git('log', '-1', '--format=%cI', commit, '--', path).decode().strip()
    items.append({'name':name, 'size':len(data), 'is_dir':False, 'modified':modified,
                  'hash_info':{'md5':hashlib.md5(data).hexdigest(), 'sha256':hashlib.sha256(data).hexdigest()}, 'type':0})

result = {'download_url':f'https://raw.githubusercontent.com/BearHero520/UFI-TOOLS-PLUGINS/{commit}/ufi-tools-plugins',
          'res':{'code':200, 'message':'success', 'data':{'content':items, 'total':len(items), 'readme':'', 'write':False}}}
(ROOT/'store.json').write_text(json.dumps(result, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
assert len(items) == len(set(i['name'] for i in items))
assert all(i['hash_info']['md5'] and i['modified'] for i in items)
print(f'Built store.json: {len(items)} entries, pinned download commit {commit}')
