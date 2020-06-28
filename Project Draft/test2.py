potential_triangles = []

for i in range(17):
    angles = [0, 0, 0]
    for j in range(2):
        angles[0] = (i+1)*10
        if 180 % (i + 1) == 0:
            angles[1] = 180/(i+1)/2 + j*5
        else:
            angles[1] = 55 + j*5
    angles[2] = 180 - sum(angles)
    potential_triangles.append(angles)

potential_triangles.append([50, 50, 80])
potential_triangles.append([60, 60, 60])
potential_triangles.append([20, 20, 140])

with open("input1.csv", "w") as f:
    for angles in potential_triangles:
        f.write(str(angles[0]) + "," + str(angles[1]) +  "," + str(angles[2]) + "\n")