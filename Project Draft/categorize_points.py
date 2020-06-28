def categorize_points(input_coordinates, lines_polygon, min_x, min_y, max_x, max_y):
    output = []
    for i in input_coordinates:
        if i[0] < min_x or i[0] > max_x:
            output.append("outside")

        elif i[1] < min_y or i[1] > max_y:
            output.append("outside")
        else:
            for l in lines_polygon:
                if i[0]



    return output