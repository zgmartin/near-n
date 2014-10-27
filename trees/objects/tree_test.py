import unittest
from tree import Tree

class TreeTest(unittest.TestCase):

    def setUp(self):
        self.t = Tree(0)
        self.val = 1
        self.LEFT = 0
    
    def append_test(self):
        self.t.append(self.val)
        self.assertEquals(self.val, self.t.ptr.children[0].data)

    def forward_test(self):
        self.t.append(self.val)
        self.t.forward(self.LEFT)
        self.assertEquals(self.val, self.t.ptr.data)
    
    def back_test(self):
        self.t.append(self.val)
        self.t.forward(self.LEFT)
        self.t.back()
        self.assertEquals(self.t.root, self.t.ptr)

    def reset_test(self):
        self.t.append(self.val)
        self.t.forward(self.LEFT)
        self.t.append(self.val)
        self.t.forward(self.LEFT)
        self.t.reset()
        self.assertEquals(self.t.root, self.t.ptr)

if __name__ == '__main__':
    unittest.main()