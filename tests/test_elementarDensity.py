import unittest
import pathlib
import sys
import math

sys.path.append('./lib/')
from elementarDensity import elementarDensity
from shimadzu import parseCsv
from winqxas import parseTxt

# test data
csv=pathlib.Path('data/ghana/EDX720/AFR390.20110406223141.csv').read_text()
txt1=pathlib.Path('data/ghana/winqxas/txt1/[1]AFR39020110406223141.txt').read_text()

irradiation_parameters = parseCsv(csv)   
txt1_content = parseTxt(txt1)

peaks1 = txt1_content['K']['peaks'] 
errors1 = txt1_content['K']['errors']
 
i=irradiation_parameters['current']
t=irradiation_parameters['livetime']

N=float(peaks1[11])

class calculateResponseFactorTest(unittest.TestCase):

    def test_11(self):
        testcase = elementarDensity(N,0.00034021562,i,t)
        calculated = N/(0.00034021562*i*t)
        self.assertAlmostEqual(testcase,calculated)

if __name__ == '__main__':
    unittest.main()
