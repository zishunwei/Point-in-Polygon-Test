a = ['1', '2', '3']

print(a[1:])
b = []
for i in a:
    i = float(i)
    b.append(i)

a = b
print(a)
