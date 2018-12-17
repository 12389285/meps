import matplotlib.pyplot as plt

def plot_scores(points, iterations, title):
    """
    This function takes the list of scores and iterations and retrun a plot.
    """

    # plot figure
    ymin = 0
    ymax = max(points) + 100
    xmin = 0
    xmax = iterations
    plt.plot(range(0, iterations), points)
    plt.axis([xmin, xmax, ymin, ymax])
    plt.title(title)
    plt.xlabel('Iterations')
    plt.ylabel('Points')

    return plt.show()
