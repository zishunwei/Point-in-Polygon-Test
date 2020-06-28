print("read input.csv")
#
input_id = []
input_x_coordinates = []
input_y_coordinates = []

with open("input.csv", "r") as i:
    for line in i.readlines():
        id = line.split(',')[0]
        input_id.append(id)

with open("input.csv", "r") as i:
    for line in i.readlines():
        x = line.split(',')[1]
        input_x_coordinates.append(x)

with open("input.csv", "r") as i:
    for line in i.readlines():
        y = line.split(',')[2]
        input_y_coordinates.append(y)


input_id = [float(i) for i in input_id[1:]]
input_x_coordinates = [float(i) for i in input_x_coordinates[1:]]
input_y_coordinates = [float(i) for i in input_y_coordinates[1:]]



print(input_id)
print(input_x_coordinates)
print(input_y_coordinates)



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

plotter.add_point(input_x_coordinates, input_y_coordinates)
plotter.show()
