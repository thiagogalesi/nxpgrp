import unittest
import shutil
import tempfile
import os
import os.path
from nxgr.file_reader import FileReader
from nxgr.file_finder import FileFinder

class TestFileReader(unittest.TestCase):

    def setUp(self):
        self.temp = tempfile.NamedTemporaryFile('w+t')
        self.fr = FileReader('pattern','negative')

    def test_search(self):
        self.temp.write('line1 pattern\n')
        self.temp.write('line2 pattern negative\n')
        self.temp.write('line3 negative\n')
        self.temp.write('line4\n')
        self.temp.flush()
        self.temp.seek(0)
        data = self.fr.process_file(self.temp)
        self.assertEquals(len(data), 1)
        self.assertTrue('line1' in data[0]['text'])

    def tearDown(self):
        self.temp.close()

class TestFileFinder(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.mkdtemp()

    def _file_name_full(self, file_name):
        return os.path.join(self.temp_dir, file_name)

    def test_find_simple(self):
        f1 = open(self._file_name_full('right'), 'w').close()
        f1 = open(self._file_name_full('wrong'), 'w').close()
        ff = FileFinder('right','wrong')
        files = ff.read_directory([self.temp_dir])
        self.assertTrue('right' in files[0])
        self.assertFalse([f for f in files if 'wrong' in f])


    def tearDown(self):
        shutil.rmtree(self.temp_dir)

if __name__=='__main__':
    unittest.main()
