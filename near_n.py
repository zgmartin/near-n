from data import Data
from kd_tree import KDTree
from collections import Counter
from view import plot
import sys
import time

def train_len(start, end, inc):
    train_len = []
    
    while start<end:
        start*=inc
        train_len.append(start)
    train_len.append(end)

    return train_len

def errors(kd, train_len, train, test):
    """
    Records test error rate on specific kd-tree trained.
        
        kd      [instance of kd]
        trains  [training list]
        train   [train data]
        test    [test data]
    """
    errors = []    

    #trains kd-tree
    for x in train_len:
        error=0
        kd.build_tree(train.data.keys()[:x])

        #tests data on kd-tree
        for y in test.data.keys():
            
            #finds nearest neighbors
            nearest = kd.near_search(y, kd.root, nearest={})

            #classifies nearest neighbors 
            classes=[]
            for i in nearest.values():
                classes.append(train.data[i])   
            
            #print classes
            #print nearest.keys()
            #mode of nearest classification
            mode = Counter(classes).most_common()[0][0]
            #test classification 
            clas = test.data[y]
            #print clas
            #time.sleep(1)

            #tests if error in kd-tree classification with test classification
            if mode != clas:
                error+=1

        error_rate =(float(error)/len(test.data))*100
        print 'x:', x
        print 'y:', error
        print 'error:', error_rate
        errors.append(error_rate)
        kd.clear()

    return errors

def nearest_n(train_file, test_file):
    """
    Performs Nearest Neighbor on data.

        builds kd-tree          [train]
        nearest neighbor        [test]

        plots error             [results]
    """

    train = Data()
    test = Data()

    kds = [KDTree(1,'dc')]
        
    #train
    train.extract(train_file)
    #x = train_len(1,len(train.data),10)
    x=[10,100,500,len(train.data)]
          
    #test
    ys=[]
    test.extract(test_file)
    y = errors(kds[0], x, train, test)

    #results
    plot(x, y, kds[0])  
                
if __name__ == '__main__':
    args = sys.argv[:]
    train_file = None
    test_file = None
    
    #checks for training and test files
    for x in args:
        if x.find('train')>0:
            train_file = x
        if x.find('test')>0:
            test_file=x

    if train_file!=None and test_file!=None: 
        nearest_n(train_file, test_file)
    else:
        print 'error: no test or train file'