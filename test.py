import unittest
import tempfile
from nxgr.file_reader import FileReader

class TestFileReader(unittest.TestCase):

    def setUp(self):
        self.temp = tempfile.NamedTemporaryFile()
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

if __name__=='__main__':
    unittest.main()
