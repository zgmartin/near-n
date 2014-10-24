from matplotlib import pyplot

def plot(x, y, kd=None):

    #labels
    name = 'kd'+ str(kd.neighbors)
    pyplot.title(name + ' Nearest Neighbor')
    pyplot.xlabel('training examples')
    pyplot.ylabel('error rate %')

    pyplot.plot(x, y, 'ro', x, y, 'b-', label=name)

    pyplot.show()

