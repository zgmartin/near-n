class vector(tuple):
    """
    A vector is a mathematically defined concept on operators + *.

    vector properties:

        commutativity: 
            v + u  = u + v 
        associativity:
            (v + u) + w = v + (u + w)
        distributive:
            a(v + u) = av + au  (a + b)v = av + bv
        identity:
            v + 0 = v
        inverse:
            v + w  = 0 
    """

    #operations
    def __add__(self, vec):
        """
        Overrides (+) operator.

        def: vector addition.
            v, u in V
            v + u = v1+u1, ..., vn+un
        """
        return vector(x + y for x, y in zip(self, vec))

        

    def __sub__(self, vec):
        """
        Overrides (-) operator.

        def: vector subtraction
            v, u in V
            v - u = v1-u1, ..., vn-un
        """
        return vector(x - y for x, y in zip(self, vec))

    
    #multiplication [not unique so cannot override (*) operator]
    def __mul__(self, vec):
        """
        Overrides (*) operator.
        """

        return self.dot(vec)
        
    def dot(self, vec):
        """
        Dot Product:
            a transformation of two vectors to a scalar.

        def: dot product
             v*u = v1*u1 + ... + vn*un
        """        
        ans = 0
        for x, y in zip(self, vec):
            ans += x * y
        
        return ans
