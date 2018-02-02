import unittest
import pathlib
import sys

# importing parseCsvShimadzu  
sys.path.append('../src')
from parseCsvShimadzu import parseCsvShimadzu

# test data
file_path='data/ghana/EDX720/AFR390.20110406223141.csv'
file_content = pathlib.Path(file_path).read_text()

class Test_parseCsvShimadzu(unittest.TestCase):

    def test_sample(self):
        self.assertEqual(parseCsvShimadzu(file_content)['sample'],"AFR390")

    def test_current(self):
        self.assertEqual(parseCsvShimadzu(file_content)['current'],1000)

    def test_livetime(self):
        self.assertEqual(parseCsvShimadzu(file_content)['livetime'],959)

if __name__ == '__main__':
    unittest.main()
