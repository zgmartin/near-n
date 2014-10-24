from data import Data
from kd_tree import KDTree

kd = KDTree(2)
d = Data()
d.extract('data/test.dat')
print d.data
kd.build_tree(d.data.keys()[:7])
print kd
print kd.near_search((7,7), kd.root)
#print kd
