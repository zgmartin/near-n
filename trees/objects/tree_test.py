import unittest
from tree import tree
from node import node

class TreeTest(unittest.TestCase):

    def setUp(self):
        self.t = tree(0)
        self.val = 1
        
    def add_test(self):
        self.t + self.val
        self.assertEquals(self.val, self.t.ptr.children[0].data)

    def forward_test(self):
        self.t + self.val
        self.t.forward(0)
        self.assertEquals(self.val, self.t.ptr.data)
    
    def back_test(self):
        self.t + self.val
        self.t.forward(0)
        self.t.back()
        self.assertEquals(0, self.t.ptr.data)

if __name__ == '__main__':
    unittest.main()