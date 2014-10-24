class node:
    """A generalized node structure.
       
       data             [information contained in node]
       n children       [generalization]

    """

    def __init__(self, data=None, parent=None):
        self.data = data
        self.parent = parent
        self.children = []

    def __add__(self, data):
        """Adds child to self."""
        
        #appending nodes
        if isinstance(data, node):
            self.children.append(data)
        else:    
            n = node(data, self)
            self.children.append(n)

    def __eq__(self, node):
        if(self.data == node.data):
            return True
        else:
            return False

    def __str__(self):
        return str(self.data)
