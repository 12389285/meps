import matplotlib.pyplot as plt

def plot_scores(points, iterations, title):
    """
    This function takes the list of scores and iterations and retrun a plot.
    """

    # plot figure
    if min(points) > 0:
        print("ja")
        ymin = 0
    if min(points) < 0:
        print("nee")
        ymin = -400
    ymax = max(points) + 100
    xmin = 0
    xmax = len(points)
    plt.plot(range(0, xmax), points)
    plt.axis([xmin, xmax, ymin, ymax])
    plt.text(xmax + 1, min(points), min(points))
    plt.title(title)
    plt.xlabel('Iterations')
    plt.ylabel('Points')

    return plt.show()
