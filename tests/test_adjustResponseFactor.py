import unittest
import pathlib
import sys

# importing parseCsvShimadzu  
sys.path.append('./elemental-analysis-scripts')
from fitResponseFactor import fitResponseFactor
from fitResponseFactor import plotFit

# test data
file_path='./data/ghana/calibration/K.csv'
file_content = pathlib.Path(file_path).read_text()

class adjustResponseFactorTest(unittest.TestCase):

    def test_sample(self):
        plotFit(file_content,start=11.0,end=42.0,degree=9)
        self.assertEqual(None,None)

if __name__ == '__main__':
    unittest.main()
