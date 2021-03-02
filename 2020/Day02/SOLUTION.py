file = open('input.txt', 'r')

line = file.readlines()

lines = []

for x in line:
    lines.append(x)


def digitsIntoOneNumber(listOfDigigt):
    number = 0
    if len(listOfDigigt) == 2:
        number = (listOfDigigt[0] *10) + listOfDigigt[1]
    elif len(listOfDigigt) == 1:
        number = listOfDigigt[0]
    return number

def checkCorrectPasswordOne(oneLineTuple):
    minimum = oneLineTuple[0]
    maximum = oneLineTuple[1]
    letter = oneLineTuple[2]
    password = oneLineTuple[3]
    count = 0
    correctPassword = False

    for x in range(len(password)):
        if password[x] == letter:
            count += 1
    
    if minimum <= count <= maximum:
        correctPassword = True
    
    return correctPassword

def checkCorrectPasswordTwo(oneLineTuple):
    position1 = oneLineTuple[0] - 1 
    position2 = oneLineTuple[1] - 1
    letter = oneLineTuple[2]
    password = oneLineTuple[3]
    correctPassword = False

    if (password[position1] == letter and password[position2] != letter) or (password[position1] != letter and password[position2] == letter):
        correctPassword = True

    return correctPassword 

def countCorrectPassword(lines, part):

    answerToPartOne = 0
    answerToPartTwo = 0

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
	
        oneLineTuple = (digitsIntoOneNumber( [int(x) for x in firstNumber] ), digitsIntoOneNumber( [int(x) for x in secondNumber] ), [str(x) for x in letter][0], [str(x) for x in password])
        
        if checkCorrectPasswordOne(oneLineTuple) and part == 1:
            answerToPartOne += 1
        
        if checkCorrectPasswordTwo(oneLineTuple) and part == 2:
            answerToPartTwo += 1
    
    if part == 1:
        return answerToPartOne
    
    if part == 2:
        return answerToPartTwo

    return 0

print(f"Part 1: ",countCorrectPassword(lines, 1))
print(f"Part 2: ",countCorrectPassword(lines, 2))
