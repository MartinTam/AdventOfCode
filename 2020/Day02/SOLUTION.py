file = open('input.txt', 'r')

line = file.readlines()

lines = []

for x in line:
    lines.append(x)


def numberIntoDigit(listOfDigigt):
    number = 0
    if len(listOfDigigt) == 2:
        number = (listOfDigigt[0] *10) + listOfDigigt[1]
    elif len(listOfDigigt) == 1:
        number = listOfDigigt[0]
    return number

def createListOfTuples(lines):

    listOfTuples = []

    for x in lines:
        firstNumber = []
        secondNumber = []
        letter = []
        password = []
        rememberMinusSign = 0
        rememberSpace = 0
        for i in range(3):
            if x[i] != '-':
                firstNumber.append(x[i])
            else:
                rememberMinusSign = i
                break
        
        for i in range(rememberMinusSign + 1, rememberMinusSign + 4):
            if x[i] != ' ':
                secondNumber.append(x[i])
            else:
                rememberSpace = i
                break
        letter.append(x[rememberSpace+1])

        for i in range(rememberSpace + 4, len(x)-1):
            password.append(x[i])
	
        oneLineTuple = (numberIntoDigit( [int(x) for x in firstNumber] ), numberIntoDigit( [int(x) for x in secondNumber] ), [str(x) for x in letter][0], [str(x) for x in password])
        listOfTuples.append(oneLineTuple)
    
    return listOfTuples



createListOfTuples(lines)
