class Geometry:
    def __init__(self, name):
        self.name = name
    def get_name(self):
        return self.name

class Point(Geometry):
    def __init__(self, name, x, y, category = 'None'):
        super().__init__(name)
        self.__x = x
        self.__y = y
        self.__category = category

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def get_category(self):
        return self.__category

    def set_category(self, category):
        self.__category = category


class Line(Geometry):
    def __init__(self, name, point_1, point_2):
        super().__init__(name)
        self.__point_1 = point_1
        self.__point_2 = point_2

    def get_point(self):
        return(self.__point_1, self.__point_2)


class Polygon(Geometry):
    def __init__(self, name, points_list):
        super().__init__(name)
        self.__points_list = points_list

    def get_points_list(self):
        return self.__points_list

    def lines(self):
        res = []
        points = self.get_points_list()
        point_a = points[0]
        for point_b in points[1:]:
            res.append(Line(point_a.get_name() + "-" + point_b.get_name(), point_a, point_b))
            point_a = point_b
        res.append(Line(point_a.get_name() + "-" + points[0].get_name(), point_a, points[0]))
        return res


class List():
    def __init__(self, number):
        self.number = number

    def minimum(self):
        res = self.number[0]
        for v in self.number[1:]:
            if v < res:
                res = v
        return res

    def maximum(self):
        res = self.number[0]
        for v in self.number[1:]:
            if v > res:
                res = v
        return res


class Classifier():

    def __init__(self, name, input_points_list, polygon):
        self.__name = name
        self.__input_points_list = input_points_list
        self.__polygon = polygon

    def get_input_points_list(self):
        return self.__input_points_list

    def get_polygon(self):
        return self.__polygon


    def min_bounding_rectangle_test(self):

        self.__polygon_points_list = self.__polygon.get_points_list()


        polygon_x_coordinates = []
        polygon_y_coordinates = []

        for i in self.__polygon_points_list:
            polygon_x_coordinates.append(i[0])
            polygon_y_coordinates.append(i[1])


        list_polygon_x = List(polygon_x_coordinates)
        list_polygon_y = List(polygon_y_coordinates)

        min_x = list_polygon_x.minimum()
        min_y = list_polygon_y.minimum()
        max_x = list_polygon_x.maximum()
        max_y = list_polygon_y.maximum()


        for i in self.__input_points_list:
            if i.get_x() < min_x or i.get_x() > max_x:
                i.set_category("Outside")

            elif i.get_y() < min_y or i.get_y() > max_y:
                i.set_category("Outside")

            else:
                i.set_category("None")

        output_mbr = self.__input_points_list

        return output_mbr


    def compute_y(self, x1,y1,x2,y2,x3):
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2
        self.__x3 = x3
        br1 = self.__x3 - self.__x1
        br2 = self.__x2 - self.__x1
        br3 = self.__y2 - self.__y1
        y = (br1 / br2) * br3 + self.__y1
        return y



    def point_on_line(self):
# arguments are points to be tested,
# (x1,y1,x2,y2) define the line (lines of polygon)
# x3,y3 define the point to be tested (input points)

        self.__polygon_lines_list = self.__polygon.lines()

        for i in
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2
        self.__x3 = x3
        self.__y3 = y3
        if not self.__y1 <= self.__y3 <= self.__y2 or self.__y2 <= self.__y3 <= self.__y1:
            return False
        elif not self.__x1 <= self.__x3 <= self.__x2 or self.__x2 <= self.__x3 <= self.__x1:
            return False
        elif self.__x1 == self.__x2 and self.__x3 == self.__x1:
            return True
        elif self.__x2 != self.__x1 and self.compute_y(self.__x1, self.__y1, self.__x2, self.__y2, self.__x3) == self.__y3:
            return True
        else:
            return False




print("read polygon.csv")

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


polygon_id = [int(i) for i in polygon_id[1:]]
polygon_x_coordinates = [float(i) for i in polygon_x_coordinates[1:]]
polygon_y_coordinates = [float(i) for i in polygon_y_coordinates[1:]]

#Turble Pair
polygon_xy_coordinates = polygon_x_coordinates + polygon_y_coordinates

n = 0
polygon_coordinates = []
for i in polygon_x_coordinates:
    r = (polygon_xy_coordinates[n], polygon_xy_coordinates[n + len(polygon_x_coordinates)])
    polygon_coordinates.append(r)
    n = n + 1

polygon = Polygon("polygon", polygon_coordinates)








print("read input.csv")

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



input_id = [int(i) for i in input_id[1:]]
input_x_coordinates = [float(i) for i in input_x_coordinates[1:]]
input_y_coordinates = [float(i) for i in input_y_coordinates[1:]]

#Turble Pair
input_xy_coordinates = input_x_coordinates + input_y_coordinates

n = 0
input_coordinates = []
for i in input_x_coordinates:
    r = (input_xy_coordinates[n], input_xy_coordinates[n + len(input_x_coordinates)])
    input_coordinates.append(r)
    n = n + 1

input_points_list = []
for i in input_coordinates:
    p = Point("Point", i[0], i[1])
    input_points_list.append(p)







print("categorize points")

mbr_classifier = Classifier("Point In Polygon Classifier", input_points_list, polygon)
output = mbr_classifier.min_bounding_rectangle_test()






print("write output.csv")

with open("output.csv", "w") as f:
    f.write("id" + "," + "category" + "\n")
    n = 1
    for i in output:
        f.write(str(n) + "," + i.get_category() + "\n")
        n = n + 1



