import unittest
import pathlib
import sys
import math

sys.path.append('../')
from blankCorrection import blankCorrection
from parseCsvShimadzu import parseCsvShimadzu
from parseTxtWinQxas import parseTxtWinQxas

# test data
file1_txt='data/ghana/blank/winqxas/[1]GPE 771 MS20100713123803.txt'
file2_txt='data/ghana/blank/winqxas/[1]GPE 774 MS20100713133258.txt'
file3_txt='data/ghana/blank/winqxas/[1]GPE 777 MS20100713142724.txt'

txts = {
    'file1': pathlib.Path(file1_txt).read_text(),
    'file2': pathlib.Path(file2_txt).read_text(),
    'file3': pathlib.Path(file3_txt).read_text()
}

file1_csv='data/ghana/blank/EDX720/GPE 771 MS.20100713123803.csv'
file2_csv='data/ghana/blank/EDX720/GPE 774 MS.20100713133258.csv'
file3_csv='data/ghana/blank/EDX720/GPE 777 MS.20100713142724.csv'

csvs = {
    'file1': pathlib.Path(file1_csv).read_text(),
    'file2': pathlib.Path(file2_csv).read_text(),
    'file3': pathlib.Path(file3_csv).read_text()
}

# current * live time for each file
it1 = 1000 * 959
it2 = 1000 * 960
it3 = 1000 * 959

# all lists above indexed by file names
peaks = {}
errors = {}
irradiation_parameters = {}

# parser files
keys = csvs.keys() # or txts.keys()
for key in keys:
    irradiation_parameters[key] = parseCsvShimadzu(csvs[key])   
    txt_content = parseTxtWinQxas(txts[key])
    peaks[key] = txt_content['peaks'] 
    errors[key] = txt_content['errors']

class Test_blankCorrection(unittest.TestCase):

    def test_13(self):
        self.assertAlmostEqual(blankCorrection(irradiation_parameters,peaks, errors)['peaks_correction'][13],(0/it1 + 226/it2 + 212/it3)/3)
        self.assertAlmostEqual(blankCorrection(irradiation_parameters,peaks, errors)['errors_correction'][13],(0/it1 + 68/it2 + 66/it3)/3)

    def test_26(self):
        self.assertAlmostEqual(blankCorrection(irradiation_parameters,peaks, errors)['peaks_correction'][26],(2195/it1  + 2610/it2 + 2124/it3)/3)
        self.assertAlmostEqual(blankCorrection(irradiation_parameters,peaks, errors)['errors_correction'][26],(230/it1 + 245/it2 + 234/it3)/3)
      
    def test_29(self):
        self.assertAlmostEqual(blankCorrection(irradiation_parameters,peaks, errors)['peaks_correction'][29],(7278/it1 + 7773/it2 + 7556/it3)/3)
        self.assertAlmostEqual(blankCorrection(irradiation_parameters,peaks, errors)['errors_correction'][29],(423/it1 + 449/it2 + 430/it3)/3)

if __name__ == '__main__':
    unittest.main()
