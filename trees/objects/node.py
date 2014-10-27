class Node:
    """A generalized node structure.
       
       data             [information contained in node]
       n children       [generalization]

    """

    def __init__(self, data=None, parent=None):
        self.data = data
        self.parent = parent
        self.children = []

    def __add__(self, data):
        if isinstance(data, Node):
            return self.data + data.data
        else:
            return self.data + data
            
        
    def __eq__(self, data):
        if isinstance(data, Node):
            return self.data == data.data
        else:
            return self.data == data
        
    def __ne__(self, data):
        if isinstance(data, Node):
            return self.data != data.data
        else:
            return self.data != data
             

    def __lt__(self, data):
        if isinstance(data, Node):
            return self.data < data.data
        else:
            return self.data < data
            

    def __gt__(self, data):
        if isinstance(data, Node):
            return self.data > data.data
        else:
            return self.data > data

    def __str__(self):
        return str(self.data)

    def append(self, data=None):
        """Appends data to self."""
        
        if isinstance(data, Node):
            data.parent = self
            self.children.append(data)
        else:
            n = Node(data, self)
            self.children.append(n)
    