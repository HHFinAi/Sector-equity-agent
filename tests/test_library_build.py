import importlib.util
from pathlib import Path
import tempfile
import unittest
spec=importlib.util.spec_from_file_location('builder',Path(__file__).resolve().parents[1]/'tools/library_build.py')
b=importlib.util.module_from_spec(spec);spec.loader.exec_module(b)
TEXT='# Library\n\n## Category\n\n### INIT-01  Test prompt\n\n```yaml\nid: INIT-01\n```\n\n```\n## This is inside a prompt\n```\n\n## Appendix\nPreserved content.\n'
class BuildTests(unittest.TestCase):
    def test_roundtrip(self): self.assertEqual(''.join(x['content'] for x in b.split_text(TEXT,1)),TEXT)
    def test_fenced_heading_not_section(self): self.assertIn('## This is inside',next(x['content'] for x in b.split_text(TEXT,1) if x['id']))
    def test_count_guard(self):
        with self.assertRaises(ValueError): b.split_text(TEXT,2)
    def test_duplicate_guard(self):
        with self.assertRaises(ValueError): b.split_text(TEXT+TEXT,2)
    def test_metadata_match(self):
        with self.assertRaises(ValueError): b.split_text(TEXT.replace('id: INIT-01','id: INIT-02'),1)
    def test_unclosed_fence(self):
        with self.assertRaises(ValueError): b.split_text(TEXT+'```\n',1)
    def test_path_escape(self):
        with tempfile.TemporaryDirectory() as d:
            with self.assertRaises(ValueError): b.safe_path(Path(d),'../outside')
    def test_init_build_drift(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d);(root/'library').mkdir();(root/'library/healthcare_prompt_library_v1.4.md').write_bytes(TEXT.encode())
            b.initialize(root,1);b.initialize(root,1)
            part=root/'prompts/INIT-01.md';part.write_text(part.read_text()+'New content.\n')
            with self.assertRaises(ValueError): b.check(root)
            b.build(root);b.check(root)
    def test_crlf_preserved(self):
        text=TEXT.replace('\n','\r\n');self.assertEqual(''.join(x['content'] for x in b.split_text(text,1)),text)

if __name__=='__main__': unittest.main()
