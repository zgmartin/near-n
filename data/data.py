from lin_alg import Vector

class Data:
    """
    Extracts data and manipulate data.
    """

    def __init__(self):
        self.data = {}                #for classification lookups

    def extract(self, file_name):
        """
        Extracts data from text file.
        """

        with open(file_name) as f:
        
            for line in f:
                s = line.split()      #parses data in string
                self.filter_data(s)   #filters data

    def filter_data(self, data):
        """
        Filters relevant data from list.
        """

        tup = map(int, tuple(data))   #transforms char->int
        clas = tup.pop()              #classification
        vec = Vector(tup)             #image vector       
        
        self.data[vec]=clas           #dictionary lookup