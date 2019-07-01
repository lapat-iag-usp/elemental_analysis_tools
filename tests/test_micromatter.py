import unittest
import pathlib
import sys

# importing parseCsvShimadzu  
sys.path.append('./eas')
import micromatter

# test data
file_path='data/calibration/micromatter-table-iag.csv'
file_content = pathlib.Path(file_path).read_text()

class MicromatterTest(unittest.TestCase):

    def test_34662(self):
        Na = micromatter.get(34662,file_content)[11]
        Cl = micromatter.get(34662,file_content)[17]
        total = micromatter.get(34662,file_content)['total']

        self.assertEqual(Na,19.5899428492)
        self.assertEqual(Cl,30.2100571508)
        self.assertEqual(total,49.8)

if __name__ == '__main__':
    unittest.main()
  
