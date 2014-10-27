from node import Node

class Tree:
    """
    A generalized tree with n children.

        root        [the root node] 
        ptr         [a pointer to current position on tree]
    """

    def __init__(self, data=None):
        self.root = Node(data)
        self.ptr = self.root

    def __str__(self, level=0, node=None):
        
        if level==0:            #init root as start 
            node=self.root
        
        s = '\t' * level + str(node.data) + '\n'
        for child in node.children:
            s+= self.__str__(level+1,child)
       
        return s
        
    def append(self, data):
        """Inserts data into pointer location on tree."""
        
        self.ptr.append(data)

    def forward(self, pos):
        """Moves pointer to a specific child node on the tree."""

        self.ptr = self.ptr.children[pos]

    def back(self):
        """Moves pointer back to parent."""

        self.ptr = self.ptr.parent

    def reset(self):
        """Resets pointer to root node."""
        
        self.ptr = self.root

    def clear(self):
        """Removes all nodes from tree by setting root to new Node"""

        self.root = Node()