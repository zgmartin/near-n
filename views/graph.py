from matplotlib import pyplot

def plot(x, y):

    #labels
    pyplot.title('Nearest Neighbor')
    pyplot.xlabel('training examples')
    pyplot.ylabel('error rate %')

    pyplot.plot(x, y, 'ro', x, y, 'b-')

    pyplot.show()

