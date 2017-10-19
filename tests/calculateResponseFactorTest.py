import unittest
import pathlib
import sys
import math

sys.path.append('../src')
from calculateResponseFactor import calculateResponseFactor
from blankCorrection import blankCorrection
from parseCsvShimadzu import parseCsvShimadzu
from parseTxtWinQxas import parseTxtWinQxas

# test data
micromatter=pathlib.Path('data/calibration/micromatter_IAGUSP.csv').read_text()
csv_34671=pathlib.Path('data/calibration/ti_34671.20131008205253.csv').read_text()
txt_34671=pathlib.Path('data/calibration/ti_3467120131008205253.txt').read_text()

irradiation_parameters = parseCsvShimadzu(csv_34671)   
txt_content = parseTxtWinQxas(txt_34671)
peaks = txt_content['peaks'] 
errors = txt_content['errors']
 
i=irradiation_parameters['current']
t=irradiation_parameters['livetime']
N=peaks[22]
print(micromatter)

class Test_blankCorrection(unittest.TestCase):

    def test_Ti(self):
        self.assertAlmostEqual(calculateResponseFactor(N,49.4,i,t),469290/(268*179*49.4))

if __name__ == '__main__':
    unittest.main()
