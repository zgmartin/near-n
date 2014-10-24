import unittest
from data import Data

class DataTest(unittest.TestCase):

    def setUp(self):
        self.d = Data()
        self.file_name = 'test.dat'

    def extract_test(self):
        ans = [(2, 3), (5, 4), (9, 6), (4, 7), (8, 1), (7, 2)]
        self.d.extract(self.file_name)
        self.assertEquals(ans, self.d.data)



if __name__ == '__main__':
    unittest.main()