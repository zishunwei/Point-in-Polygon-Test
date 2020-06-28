print("read polygon.csv")

#
polygon_id = []
polygon_x_coordinates = []
polygon_y_coordinates = []

with open("polygon.csv", "r") as p:
    for line in p.readlines():
        id = line.split(',')[0]
        polygon_id.append(id)

with open("polygon.csv", "r") as p:
    for line in p.readlines():
        x = line.split(',')[1]
        polygon_x_coordinates.append(x)

with open("polygon.csv", "r") as p:
    for line in p.readlines():
        y = line.split(',')[2]
        polygon_y_coordinates.append(y)


polygon_id = [float(i) for i in polygon_id[1:]]
polygon_x_coordinates = [float(i) for i in polygon_x_coordinates[1:]]
polygon_y_coordinates = [float(i) for i in polygon_y_coordinates[1:]]


print(polygon_id)
print(polygon_x_coordinates)
print(polygon_y_coordinates)


from collections import OrderedDict

import matplotlib
import matplotlib.pyplot as plt

matplotlib.use('TkAgg')


class Plotter:

    def __init__(self):
        plt.figure()

    def add_polygon(self, xs, ys):
        plt.fill(xs, ys, 'lightgray', label='Polygon')

    def add_point(self, x, y, kind=None):
        if kind == "outside":
            plt.plot(x, y, "ro", label='Outside')
        elif kind == "boundary":
            plt.plot(x, y, "bo", label='Boundary')
        elif kind == "inside":
            plt.plot(x, y, "go", label='Inside')
        else:
            plt.plot(x, y, "ko", label='Unclassified')

    def show(self):
        handles, labels = plt.gca().get_legend_handles_labels()
        by_label = OrderedDict(zip(labels, handles))
        plt.legend(by_label.values(), by_label.keys())
        plt.show()



plotter = Plotter()
plotter.add_polygon(polygon_x_coordinates, polygon_y_coordinates)
plotter.show()


