import unittest
from kd_tree import KDTree

class KDTreeTest(unittest.TestCase):

    def setUp(self):
        self.data = [(1,),(2,),(0,)]    
        self.kd_tree = KDTree() 

    def median_test(self):
        median = self.kd_tree.median(self.data)
        m = self.data[len(self.data)/2]
        
        self.assertEquals(m, median)

    def insert_search_test(self):
        def f(data):
            for e in data:
                self.kd_tree.insert_search(e, self.kd_tree.root)

        f(self.data)

        self.assertEquals(self.data[0], self.kd_tree.root.data)
        self.assertEquals(self.data[1], self.kd_tree.root.children[1].data)
        self.assertEquals(self.data[2], self.kd_tree.root.children[0].data)

    def insert_medians_test(self):
        self.data.sort()
        self.kd_tree.insert_medians(self.data)

        self.assertEquals(self.data[0], self.kd_tree.root.data)
        self.assertEquals(self.data[1], self.kd_tree.root.children[1].data)
        self.assertEquals(self.data[2], self.kd_tree.root.children[0].data)

    
if __name__ == '__main__':
    unittest.main()