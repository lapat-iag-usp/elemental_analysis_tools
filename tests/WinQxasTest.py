import unittest
import pathlib
import sys
import math

# importing parseCsvShimadzu  
sys.path.append('../')
from WinQxas import parseTxt

# test data
file_path='data/ghana/winqxas/txt1/[1]AFR39020110406223141.txt'
file_content = pathlib.Path(file_path).read_text()

# test element with line K and L in the same spectra
file2_path='data/calibration/txt/34691.txt'
file2_content = pathlib.Path(file2_path).read_text()

class WinQxasTest(unittest.TestCase):
    def test_11(self):
        self.assertEqual(parseTxt(file_content)['K']['peaks'][11],389)
        self.assertEqual(parseTxt(file_content)['K']['errors'][11],71)

    def test_13(self):
        self.assertEqual(parseTxt(file_content)['K']['peaks'][13],8871)
        self.assertEqual(parseTxt(file_content)['K']['errors'][13],133)

    def test_14(self):
        self.assertEqual(parseTxt(file_content)['K']['peaks'][14],38268)
        self.assertEqual(parseTxt(file_content)['K']['errors'][14],282)

    def test_22(self):
        self.assertEqual(parseTxt(file_content)['K']['peaks'][22],19355)
        self.assertEqual(parseTxt(file_content)['K']['errors'][22],222)
        
    def test_56(self):
        self.assertEqual(parseTxt(file_content)['L']['peaks'][56],1182)
        self.assertEqual(parseTxt(file_content)['L']['errors'][56],214)

    def test_42(self):
        self.assertEqual(parseTxt(file2_content)['K']['peaks'][42],372924)
        self.assertEqual(parseTxt(file2_content)['L']['peaks'][42],30490)
        self.assertEqual(parseTxt(file2_content)['K']['errors'][42],625)
        self.assertEqual(parseTxt(file2_content)['L']['errors'][42],293)

if __name__ == '__main__':
    unittest.main()
