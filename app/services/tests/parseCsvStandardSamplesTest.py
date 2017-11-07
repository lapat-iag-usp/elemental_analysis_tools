import unittest
import pathlib
import sys

# importing parseCsvShimadzu  
sys.path.append('../src')
from parseCsvStandardSamples import parseCsvStandardSamples

# test data
file_path='data/calibration/micromatter_IAGUSP.csv'
file_content = pathlib.Path(file_path).read_text()

class Test_parseCsvStandardSamples(unittest.TestCase):

    def test_sample(self):
        self.assertEqual(parseCsvStandardSamples(file_content),None)

if __name__ == '__main__':
    unittest.main()
