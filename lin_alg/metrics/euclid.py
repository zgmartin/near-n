def dist(x, y):
    """
    Euclidean Distance:
        A measurement of the difference between coordinate values.

        distance def:    
            d(x,y)^2 = (x1-y1)^2 + ... + (xn-yn)^2   [squaring avoids R and stays in I]
            
            dot product derivation:
                (x-y) = x1-y1, ..., xn-yn               [subtraction]
                (x-y)^2 = (x1-y1)^2 + ... + (xn-yn)^2   [dot product]
                (x-y)^2 = d(x,y)^2                      [equals def]

    """
   
    dist = x - y
    square_dist = dist*dist

    return square_dist