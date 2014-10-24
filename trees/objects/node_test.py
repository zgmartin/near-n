import unittest
from node import node

class NodeTest(unittest.TestCase):

    def setUp(self):
        self.root = node([1,1])
        self.child = node([2,2]) 

    def add_test(self):
        self.root + self.child
        self.assertEquals(self.child, self.root.children[0])

if __name__ == '__main__':
    unittest.main()