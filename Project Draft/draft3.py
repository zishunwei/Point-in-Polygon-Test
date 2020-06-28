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
    r = (str(polygon_id[n]), polygon_xy_coordinates[n], polygon_xy_coordinates[n + len(polygon_x_coordinates)])
    polygon_coordinates.append(r)
    n = n + 1

polygon = Polygon(polygon_coordinates)






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





print("categorize points")



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

    def set_category(self):
        return self.__category


class Line(Geometry):
    def __init__(self, name, point_1, point_2):
        super().__init__(name)
        self.__point_1 = point_1
        self.__point_2 = point_2

    def get_point(self):
        return(self.__point_1, self.__point_2)


class Polygon(Geometry):
    def __init__(self, name, points):
        super().__init__(name)
        self.__points = points

    def get_points(self):
        return self.__points

    def lines(self):
        res = []
        points = self.get_points()
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

    def __init__(self, point, polygon):
        self.__name = name
        self.__point = point
        self.__polygon = polygon

    def min_bounding_rectangle_test(self):

        self.__point = point
        self.__polygon = polygon

        polygon_points = self.get_points(polygon)
        polygon_x_coordinates = polygon_points.get_

        list_polygon_x = List(polygon_x_coordinates)
        list_polygon_y = List(polygon_y_coordinates)

        min_x = list_polygon_x.minimum()
        min_y = list_polygon_y.minimum()
        max_x = list_polygon_x.maximum()
        max_y = list_polygon_y.maximum()

        output = []
        for i in input_coordinates:
            if i[0] < min_x or i[0] > max_x:
                output.append("Outside")

            elif i[1] < min_y or i[1] > max_y:
                output.append("Outside")

            else:
                output


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



    def point_on_line(self, x1, y1, x2, y2, x3, y3):
# arguments are points to be tested,
# (x1,y1,x2,y2) define the line,
# x3,y3 define the point to be tested
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

    def line_crossing(self, x3, y3, x4, y4, x1, y1):
        # arguments are points to be tested,
        # (x3, y3, x4, y4) define the lines of poloygon,
        # (x1, y1) define the ray which is parallel with the x-axis

        if y3 == y4:
            if y1 == y3:
                if x1 <= x3 or x1 <= x4:
                    return True
                else:
                    return False
            else:
                return False

        else:
            x = (y1 - y3) * (x4 - x3) / (y4 - y3) + x3
            if y3 <= y1 <= y4 or y4 <= y1 <= y3:

                if x >= x1:
                    return True
            else:
                return False

    def categorize_points(self, input_coordinates, lines_polygon, polygon_x_coordinates, polygon_y_coordinates):
        # define Minimum Bounding Rectangle
        list_polygon_x = List(polygon_x_coordinates)
        list_polygon_y = List(polygon_y_coordinates)

        min_x = list_polygon_x.minimum()
        min_y = list_polygon_y.minimum()
        max_x = list_polygon_x.maximum()
        max_y = list_polygon_y.maximum()

        output = []
        for i in input_coordinates:
            if i[0] < min_x or i[0] > max_x:
                output.append("Outside")

            elif i[1] < min_y or i[1] > max_y:
                output.append("Outside")
            else:
                y3 = i[1]
                x3 = i[0]
                count = 0
                for j in lines_polygon:
                    if self.point_on_line(j.get_x1(), j.get_y1(), j.get_x2(), j.get_y2(), x3, y3) == True:
                        output.append("Boundary")
                        break
                    else：

                    elif self.line_crossing(j.get_x1(), j.get_y1(), j.get_x2(), j.get_y2(), x3, y3) == True:
                        count = count + 1
                        if count % 2 == 0:
                            output.append("Outside")

                    else:
                        output.append("Inside")


        return output


points_polygon = []
for name, x, y in polygon_coordinates:
    r = Point(name, x, y)
    points_polygon.append(r)

polygon = Polygon("polygon", points_polygon)
lines_polygon = polygon.lines()


point_in_polygon_classifier = Classifier("Point In Polygon Classifier")
output = point_in_polygon_classifier.categorize_points(input_coordinates, lines_polygon, polygon_x_coordinates, polygon_y_coordinates)


with open("output.csv", "w") as f:
    f.write("id" + "," + "category" + "\n")
    n = 1
    for i in output:
        f.write(str(n) + "," + i + "\n")
        n = n + 1













