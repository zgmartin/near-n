def dist(x,y):
    """
    Manhattan distance:
        The sum of the distances between two vector components.
    
        def distance:
            v = v1, ..., vn
            u = u1, ..., un
            dis(v, u) = |v1-u1| + ...+ |vn-un|
    """
    
    ab = map(abs, x-y)
    return sum(ab) 
