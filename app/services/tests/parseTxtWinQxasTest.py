import unittest
import pathlib
import sys
import math

# importing parseCsvShimadzu  
sys.path.append('../src')
from parseTxtWinQxas import parseTxtWinQxas

# test data
file_path='data/ghana/winqxas/txt1/[1]AFR39020110406223141.txt'
file_content = pathlib.Path(file_path).read_text()

class Test_parseTxtWinQxas(unittest.TestCase):

    def test_11(self):
        self.assertEqual(parseTxtWinQxas(file_content)['peaks'][11],389)
        self.assertEqual(parseTxtWinQxas(file_content)['errors'][11],71)

    def test_13(self):
        self.assertEqual(parseTxtWinQxas(file_content)['peaks'][13],8871)
        self.assertEqual(parseTxtWinQxas(file_content)['errors'][13],133)

    def test_14(self):
        self.assertEqual(parseTxtWinQxas(file_content)['peaks'][14],38268+171)
        self.assertEqual(parseTxtWinQxas(file_content)['errors'][14],math.sqrt(282**2+298**2))

    def test_22(self):
        self.assertEqual(parseTxtWinQxas(file_content)['peaks'][22],19355)
        self.assertEqual(parseTxtWinQxas(file_content)['errors'][22],222)
        
    def test_56(self):
        self.assertEqual(parseTxtWinQxas(file_content)['peaks'][56],1182)
        self.assertEqual(parseTxtWinQxas(file_content)['errors'][56],214)

if __name__ == '__main__':
    unittest.main()
