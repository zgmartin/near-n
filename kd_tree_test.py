import unittest
from kd_tree import KDTree
from lin_alg import Vector

class KDTreeTest(unittest.TestCase):

    def setUp(self):
        self.data = [Vector([1]),Vector([2]),Vector([0])]    
        self.kd_tree = KDTree() 

    def median_test(self):
        median = self.kd_tree.median(self.data)
        m = self.data[len(self.data)/2]
        
        self.assertEquals(m, median)

    def append_test(self):
        def f(data):
            for x in data:
                self.kd_tree.append(x, self.kd_tree.root)

        f(self.data)

        self.assertEquals(self.data[0], self.kd_tree.root.data)
        self.assertEquals(self.data[1], self.kd_tree.root.children[1].data)
        self.assertEquals(self.data[2], self.kd_tree.root.children[0].data)

    def append_medians_test(self):
        self.kd_tree.append_medians(self.data)

        #self.assertEquals(Vector([2]), self.kd_tree.root.data)
        #self.assertEquals(Vector([1]), self.kd_tree.root.children[1].data)
        #self.assertEquals(Vector([0]), self.kd_tree.root.children[0].data)

    def nearest_test(self):
        self.kd_tree.append_medians(self.data)

        nearest=self.kd_tree.nearest(Vector([3]), self.kd_tree.root)
        self.assertEquals(Vector([2]), nearest.values()[0])

if __name__ == '__main__':
    unittest.main()