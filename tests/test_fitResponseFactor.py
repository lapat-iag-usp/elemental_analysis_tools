import unittest
import pathlib
import sys

# importing parseCsvShimadzu  
sys.path.append('./elemental_analysis_tools')
from fitResponseFactor import fitResponseFactor
from fitResponseFactor import plotFit
from fitResponseFactor import experimentalData

# test data
file_path='./data/ghana/calibration/K.csv'
file_content = pathlib.Path(file_path).read_text()

class fitResponseFactorTest(unittest.TestCase):

    def test_11(self):
        aux = experimentalData(file_content)
        fit = fitResponseFactor(aux['Z'],aux['Y'],aux['Yerror'], start=11,end=42, degree = 9)
        export = fit['export']
        testcase = export['Y'][0]
        calculed = 0.010074417017454637
        self.assertAlmostEqual(testcase,calculed)

if __name__ == '__main__':
    unittest.main()
