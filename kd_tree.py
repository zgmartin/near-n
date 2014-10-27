from trees import Tree
from lin_alg import metrics

class KDTree(Tree):
    """
    A K-Dimensional binary search tree.
        
        root        [tree root] 
        neighbors   [number of neighbors]

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
        self.LEFT = 0
        self.RIGHT = 1
         
        Tree.__init__(self)

    def build_tree(self, data):
        """Builds kd-tree from data."""

        data.sort()                     #sort data
        self.append_medians(data)       #inserts data set into tree  

    def append_medians(self, data):
        """Inserts data set into kd-tree based on median."""
        
        #base case
        if len(data) == 0:
            return

        median = self.median(data)
        data.remove(median)

        self.append(median, self.root)   #appends data into tree    
                    
        #inductive case
        #divide and conquer
        if 'dc' in self.opt:
            i = len(data)/2
            data = data[:i],data[i:]            #splits data into left and right
        
            self.append_medians(data[self.LEFT])                 
            self.append_medians(data[self.RIGHT])   
            
        #default
        else:    
            self.append_medians(data)
        

    def median(self, data):
        """Selects root node based on median of data."""
        
        median = data[len(data)/2]      

        return median   

    def append(self, data, node, level=0):
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
                node.append()

        #base case 
        if node == None:
            node.data = data
            return node

        #hyperplane split
        i = level%len(data)                  

        #inductive case 
        if data[i] < node.data[i]:   
            return self.append(data, node.children[self.LEFT], level+1)
        else:
            return self.append(data, node.children[self.RIGHT], level+1)
                
    

    def nearest(self, data, node, level=0, nearest={}):
        """
        Nearest neighbor search on kd-tree.

            data    [search point]
            node    [starting node]
            nearest [hashmap key:distance value:vector] 
            
            algorithm:
                move left or right based plane split
                if distance < best
                    insert current node into list 

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
            return self.nearest(data,node.children[0],level+1,nearest)    
        else:
            #branch = 1
            return self.nearest(data,node.children[1],level+1,nearest)

        #hypersphere intersection hyperplane
        #if abs(node.parent.data[i]-data[i]) < max(nearest.keys()) and node.parent not in visited:
        #    branch=(branch+1)%2
        #    node=node.parent
        #    visited.append(node)
        #    return self.nearest(data,node.children[branch],level+1,nearest,branch,visited)
