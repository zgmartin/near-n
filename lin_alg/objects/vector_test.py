import unittest
from vector import Vector

class VectorTest(unittest.TestCase):

    def setUp(self):
        self.v = Vector((1,1))
        self.u = Vector((2,2))

    def add_test(self):
        ans = Vector((3,3))
        add = self.v + self.u
        self.assertEquals(ans, add)

    def sub_test(self):
        ans = Vector((-1,-1))
        dif = self.v - self.u
        self.assertEquals(ans, dif)

    def dot_test(self):
        ans = 4
        dot = self.v.dot(self.u)
        self.assertEquals(ans, dot)

if __name__ == '__main__':
    unittest.main()
        

