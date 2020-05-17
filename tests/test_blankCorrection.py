import unittest
import pathlib
import sys
import math

sys.path.append('./elemental-analysis-scripts')
from blankCorrection import blankCorrection
from shimadzu import parseCsv
from winqxas import parseTxt

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
    irradiation_parameters[key] = parseCsv(csvs[key]) 
    txt_content = parseTxt(txts[key])
    peaks[key] = txt_content['K']['peaks'] 
    errors[key] = txt_content['K']['errors']

class blankCorrectionTest(unittest.TestCase):

    def test_13(self):
        # teste peak
        testcase = blankCorrection(irradiation_parameters,peaks, errors)['peaks_correction'][13]
        calculed = (0/it1 + 226/it2 + 212/it3)/3
        self.assertAlmostEqual(testcase,calculed)

        # test error
        testcase = blankCorrection(irradiation_parameters,peaks, errors)['errors_correction'][13]
        calculed = (0/it1 + 68/it2 + 66/it3)/3
        self.assertAlmostEqual(testcase,calculed)

    def test_26(self):
        # test peak
        testcase = blankCorrection(irradiation_parameters,peaks, errors)['peaks_correction'][26]
        calculed = (2195/it1  + 2610/it2 + 2124/it3)/3
        self.assertAlmostEqual(testcase,calculed)

        # test error
        testcase = blankCorrection(irradiation_parameters,peaks, errors)['errors_correction'][26]
        calculed = (230/it1 + 245/it2 + 234/it3)/3
        self.assertAlmostEqual(testcase,calculed)
      
    def test_29(self):
        # test peak
        testcase = blankCorrection(irradiation_parameters,peaks, errors)['peaks_correction'][29]
        calculed = (7278/it1 + 7773/it2 + 7556/it3)/3
        self.assertAlmostEqual(testcase,calculed)

        # test error
        testcase = blankCorrection(irradiation_parameters,peaks, errors)['errors_correction'][29]
        calculed = (423/it1 + 449/it2 + 430/it3)/3
        self.assertAlmostEqual(testcase,calculed)


if __name__ == '__main__':
    unittest.main()
