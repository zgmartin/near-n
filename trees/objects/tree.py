from node import node

class tree:
    """
    A generalized tree with n children.

        root        [the root node] 
        pointer     [a pointer to current position on tree]
    """

    def __init__(self, data=None):
        self.root = node(data)
        self.ptr = self.root

    def __str__(self, level=0, node=None):
        
        if level==0:            #init root as start 
            node=self.root
        
        s = '\t' * level + str(node.data) + '\n'
        for child in node.children:
            s+= self.__str__(level+1,child)
       
        return s

    def __add__(self, data):

        self.add_child(data)

    def add_child(self, data):
        """Adds child to pointer location on tree."""
        
        n = node(data, self.ptr)
        self.ptr + n

    def insert(self, data):
        """Inserts data into pointer location on tree."""
        
        self.ptr.data = data

    def forward(self, next_pos):
        """Moves pointer to a specific child node on the tree."""

        self.ptr = self.ptr.children[next_pos]

    def back(self):
        """Moves pointer back to parent."""

        self.ptr = self.ptr.parent

    def reset(self):
        """Resets pointer to root node."""
        
        self.ptr = self.root

    def clear(self):
        """Clears tree by setting root to new Node"""

        self.root = node()