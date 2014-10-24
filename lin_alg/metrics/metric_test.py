import unittest
from lin_alg.objects import vector
from lin_alg.metrics import euclid
from lin_alg.metrics import manhat

class MetricTest(unittest.TestCase):

    def setUp(self):
        self.v = vector((1,1))
        self.u = vector((3,3))

    def euclid_test(self):
        ans = 8
        self.assertEquals(ans, euclid.dist(self.v, self.u))

    def manhat_test(self):
        ans = 4
        self.assertEquals(ans, manhat.dist(self.v, self.u))

if __name__ == '__main__':
    unittest.main()