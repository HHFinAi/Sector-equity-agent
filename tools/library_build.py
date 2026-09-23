"""Losslessly split/rebuild the library into prompt files and contextual sections."""
import argparse
import hashlib
import json
from pathlib import Path
import re

PROMPT = re.compile(r'^###\s+([A-Z][A-Z0-9]*(?:-[A-Z0-9]+)*-\d{2})\s+(.+?)\s*$')


def split_text(text, expected_count):
    boundaries = [(0, None, 'Introduction')]
    offset, fence, fence_length = 0, None, 0
    for line in text.splitlines(keepends=True):
        marker = re.match(r'^\s*(`{3,}|~{3,})', line)
        if marker:
            run = marker.group(1)
            if fence is None:
                fence, fence_length = run[0], len(run)
            elif run[0] == fence and len(run) >= fence_length:
                fence = None
        elif fence is None:
            match = PROMPT.match(line.rstrip('\r\n'))
            if match:
                boundaries.append((offset, match.group(1), match.group(2)))
            elif line.startswith('## '):
                boundaries.append((offset, None, line.strip()[3:]))
        offset += len(line)
    if fence is not None:
        raise ValueError('Unclosed code fence; cannot split safely')
    pieces, ids = [], set()
    for i, (start, ident, title) in enumerate(boundaries):
        end = boundaries[i+1][0] if i+1 < len(boundaries) else len(text)
        body = text[start:end]
        if not body:
            continue
        if ident:
            if ident in ids:
                raise ValueError('Duplicate prompt ID: ' + ident)
            ids.add(ident)
            metadata = re.search(r'^```yaml\s*\r?\n(.*?)^```\s*$', body, re.M | re.S)
            if not metadata or not re.search(r'^id:\s*' + re.escape(ident) + r'\s*$', metadata.group(1), re.M):
                raise ValueError('Heading/metadata ID mismatch: ' + ident)
            path = f'prompts/{ident}.md'
        else:
            path = f'library/sections/{i:03}.md'
        pieces.append({'path':path,'id':ident,'title':title,'content':body})
    if len(ids) != expected_count:
        raise ValueError(f'Expected {expected_count} prompts, found {len(ids)}')
    if ''.join(p['content'] for p in pieces) != text:
        raise ValueError('Round-trip content mismatch')
    return pieces


def safe_path(root, relative):
    path = (root / relative).resolve()
    if not path.is_relative_to(root.resolve()):
        raise ValueError('Manifest path escapes repository')
    return path


def initialize(root, expected_count=113):
    manifest_path = root / 'library/manifest.json'
    if manifest_path.exists():
        check(root)
        return
    source = root / 'library/healthcare_prompt_library_v1.4.md'
    text = source.read_bytes().decode('utf-8')
    pieces = split_text(text, expected_count)
    for piece in pieces:
        path = safe_path(root, piece['path'])
        if path.exists():
            raise ValueError('Refusing to overwrite existing split source: ' + piece['path'])
    for piece in pieces:
        path = safe_path(root, piece['path']); path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(piece['content'].encode('utf-8'))
    manifest = {'schema_version':1,'prompt_count':expected_count,'original_sha256':hashlib.sha256(text.encode('utf-8')).hexdigest(),
                'parts':[{k:v for k,v in piece.items() if k != 'content'} for piece in pieces]}
    manifest_path.write_text(json.dumps(manifest,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    build(root)
    if (root / 'library/healthcare_prompt_library.md').read_bytes() != source.read_bytes():
        raise ValueError('Initial generated library is not byte-identical to original')
    check(root)


def assemble(root):
    manifest = json.loads((root / 'library/manifest.json').read_text(encoding='utf-8'))
    paths, ids, bodies = set(), set(), []
    for part in manifest['parts']:
        if part['path'] in paths:
            raise ValueError('Duplicate manifest path')
        paths.add(part['path'])
        body = safe_path(root,part['path']).read_bytes().decode('utf-8')
        if part['id']:
            if part['id'] in ids:
                raise ValueError('Duplicate manifest ID')
            ids.add(part['id'])
            heading = PROMPT.match(body.splitlines()[0])
            if not heading or heading.group(1) != part['id']:
                raise ValueError('Prompt file ID mismatch')
        bodies.append(body)
    if len(ids) != manifest['prompt_count']:
        raise ValueError('Prompt count mismatch')
    actual = {p.relative_to(root).as_posix() for p in (root/'prompts').glob('*.md')}
    expected = {p['path'] for p in manifest['parts'] if p['id']}
    if actual != expected:
        raise ValueError('Unlisted or missing prompt files')
    return ''.join(bodies), manifest


def build(root):
    text, _ = assemble(root)
    (root/'library/healthcare_prompt_library.md').write_bytes(text.encode('utf-8'))


def check(root):
    text, manifest = assemble(root)
    if (root/'library/healthcare_prompt_library.md').read_bytes() != text.encode('utf-8'):
        raise ValueError('Generated library is stale; run tools/library_build.py build')
    split_text(text, manifest['prompt_count'])
    print(f"Verified {manifest['prompt_count']} prompt files and lossless current rebuild")


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('command',choices=['init','build','check'])
    args = p.parse_args()
    root = Path(__file__).resolve().parents[1]
    {'init':initialize,'build':build,'check':check}[args.command](root)


if __name__ == '__main__': main()
