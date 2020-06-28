a = [(1, 2), (2, 4), (3 , 5), (1, 2)]

b = [5, 6, 7, 8]

def line_crossing(x3, y3, x4, y4, x1, y1):
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

l = line_crossing(1, 3, 2, 3, 2, 6)
print(l)

