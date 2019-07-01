import unittest
import pathlib
import sys

# importing parseCsvShimadzu  
sys.path.append('./eas')
from shimadzu import parseCsv

# test data
file_path='./data/ghana/EDX720/AFR390.20110406223141.csv'
file_content = pathlib.Path(file_path).read_text()

class ShimadzuTest(unittest.TestCase):

    def test_sample(self):
        self.assertEqual(parseCsv(file_content)['sample'],"AFR390")

    def test_current(self):
        self.assertEqual(parseCsv(file_content)['current'],1000)

    def test_livetime(self):
        self.assertEqual(parseCsv(file_content)['livetime'],959)

if __name__ == '__main__':
    unittest.main()
