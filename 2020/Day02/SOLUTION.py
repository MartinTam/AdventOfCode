file = open('input.txt', 'r')

line = file.readlines()

lines = []

for x in line:
    lines.append(x)

for i in lines:
    print(i)