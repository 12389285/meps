import matplotlib as plt




def plot_scores():

    points = []

    title = 

    # plot figure
    ymin = min(points)
    ymax = max(points)
    xmin = min(iterations)
    xmax = max(iterations)
    plt.plot(iterations, points)
    plt.axis([xmin, xmax, ymin, ymax])
    plt.title(title)
    plt.xlabel('Iterations')
    plt.ylabel('Points')

return plt.show()
