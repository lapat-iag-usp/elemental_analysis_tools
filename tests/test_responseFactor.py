import unittest
import pathlib
import sys
import math

sys.path.append('./eas')
from responseFactor import responseFactor
from shimadzu import parseCsv
from winqxas import parseTxt
import numpy as np

# test data
micromatter=pathlib.Path('data/calibration/micromatter-table-iag.csv').read_text()
csv_34671=pathlib.Path('data/calibration/2010-10/csv/34671.csv').read_text()
txt_34671=pathlib.Path('data/calibration/2010-10/txt/34671.txt').read_text()

irradiation_parameters = parseCsv(csv_34671)   
txt_content = parseTxt(txt_34671)
peaks = txt_content['K']['peaks'] 
errors = txt_content['K']['errors']
 
i=irradiation_parameters['current']
t=irradiation_parameters['livetime']
N=peaks[22]
sigma_N=errors[22]

class calculateResponseFactorTest(unittest.TestCase):

    def test_Ti(self):
        R,sigma_R = responseFactor(N,49.4,i,t,sigma_N)
        R_calculated = 454712/(268*179*49.4)
        sigma_calculated = R_calculated*np.sqrt((676/454712)**2+(0.05)**2+(0.05)**2+(0.05)**2)
        self.assertAlmostEqual(R,R_calculated)
        self.assertAlmostEqual(sigma_R,sigma_calculated)

if __name__ == '__main__':
    unittest.main()
