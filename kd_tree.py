from trees import tree
from lin_alg import metrics

class KDTree(tree):
    """
    kd-tree:

        k-dimensional binary tree
        root = median 

    options:            
        insertion:
            'dc' = divide and conquer median
            (default) median  
        
        nearest neighbor:
            'm' = manhattan distance 
            (default) euclidean
    """
    
    def __init__(self, neighbors=1, *opt):
        self.opt = opt
        self.neighbors = neighbors
         
        tree.__init__(self)

    def build_tree(self, data):
        """Builds kd-tree from data."""

        data.sort()                                      #sort data
        self.insert_medians(data)                       #inserts data set into tree  

    def insert_medians(self, data):
        """Inserts data set into kd-tree based on median."""
        
        #base case
        if len(data) == 0:
            return

        median = self.median(data)
        data.remove(median)

        self.insert_search(median, self.root)                            #searches for place to insert    
                    
        #inductive case
        #divide and conquer
        if 'dc' in self.opt:
            i = len(data)/2
            data = data[:i],data[i:]                       #splits data into left and right
        
            self.insert_medians(data[0])                    #left            
            self.insert_medians(data[1])                    #right
            
        #default
        else:    
            self.insert_medians(data)
        

    def median(self, data):
        """Selects root node based on median of data."""
        
        median = data[len(data)/2]      

        return median   

    def insert_search(self, data, node, level=0):
        """
        Searches tree for location to place data.
            
            algorithm:
                if hyperplane(element of data) is less than tree pointer element
                    move left
                else
                    move right
        """

        #creates binary devision
        if node.children == []:       
            for i in range(2): 
                node + None

        #recursion end 
        if node.data == None:
            node.data = data
            return node

        #hyperplane split
        i = level%len(data)                  

        #recursion left or right 
        if data[i] < node.data[i]:   
            return self.insert_search(data, node.children[0], level+1)
        else:
            return self.insert_search(data, node.children[1], level+1)
                
    

    def near_search(self, data, node, level=0, nearest={}):
        """
        Nearest Neighbor Search on kd-tree.

            nearest [hashmap key:distance value:vector] 
            algorithm:


            distance metrics:
                euclidean: sum((x-y)^2))
                manhattan: sum(|x-y|)
        """

        #base case
        if node.children == []:
            return nearest

        #optional metrics
        if 'm' in self.opt:
            dist = metrics.manhat.dist(node.data, data)
        else:
            dist = metrics.euclid.dist(node.data, data)

        #init nearest
        if nearest == {}:
            nearest[dist] = node.data

        #updates nearest neighbors
        if dist<max(nearest.keys()) or len(nearest)<self.neighbors:
            nearest[dist] = node.data
            if len(nearest) > self.neighbors:
                del nearest[max(nearest.keys())]
                

        #hyperplane split
        i = level%len(data)      

        #binary tree split
        if data[i] < node.data[i]:
            #branch = 0
            return self.near_search(data,node.children[0],level+1,nearest)    
        else:
            #branch = 1
            return self.near_search(data,node.children[1],level+1,nearest)

        #hypersphere intersection hyperplane
        #if abs(node.parent.data[i]-data[i]) < max(nearest.keys()) and node.parent not in visited:
        #    branch=(branch+1)%2
        #    node=node.parent
        #    visited.append(node)
        #    return self.near_search(data,node.children[branch],level+1,nearest,branch,visited)
