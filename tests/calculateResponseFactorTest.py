import unittest
import pathlib
import sys
import math

sys.path.append('../')
from calculateResponseFactor import ResponseFactor
from Shimadzu import parseCsv
from WinQxas import parseTxt

# test data
micromatter=pathlib.Path('data/calibration/micromatter.csv').read_text()
csv_34671=pathlib.Path('data/calibration/csv/34671.csv').read_text()
txt_34671=pathlib.Path('data/calibration/txt/34671.txt').read_text()

irradiation_parameters = parseCsv(csv_34671)   
txt_content = parseTxt(txt_34671)
peaks = txt_content['K']['peaks'] 
errors = txt_content['K']['errors']
 
i=irradiation_parameters['current']
t=irradiation_parameters['livetime']
N=peaks[22]

class calculateResponseFactorTest(unittest.TestCase):

    def test_Ti(self):
        testcase = ResponseFactor(N,49.4,i,t)
        calculated = 454712/(268*179*49.4)
        self.assertAlmostEqual(testcase,calculated)

if __name__ == '__main__':
    unittest.main()
