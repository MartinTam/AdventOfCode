file = open('input.txt', 'r')

line = file.readlines()

lines = []

for x in line:
    lines.append(x)

def createListOfTuples(lines):

    for x in lines:
        
        for i in range(len(x)):
            if x[i] != '-':


createListOfTuples(lines)