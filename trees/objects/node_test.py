import unittest
from node import Node

class NodeTest(unittest.TestCase):

    def setUp(self):
        self.root = Node([1,1])
        self.child = Node([2,2]) 

    def add_test(self):
        ans=[1,1,2,2]
        self.assertEquals(ans, self.root + self.child)

if __name__ == '__main__':
    unittest.main()