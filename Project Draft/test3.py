x = [1, 2, 3, 4]
y = [2, 3, 4, 5]

print(len(x))

xy = x + y
print(xy)

n = 0
coord = []
for i in x:
    r = (xy[n], xy[n + len(x)])
    coord.append(r)
    n = n + 1


print(coord)

output = []
for x in input_x:
    if x < min_x or x > max_x:
        output.append("Outside")
    else:
        output.append("Inside")
n = 0
for y in input_y:
    if y < min_y or y > max_y:
        output[n] = "Outside"
    n = n + 1
return output