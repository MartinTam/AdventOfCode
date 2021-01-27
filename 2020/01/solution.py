file = open('input.txt', 'r')

numbersSTR = file.readlines()

numbers = []

for x in numbersSTR:
    numbers.append( int(x) )

def printSets(sets):
    for i in sets:
        return i

def partOne(numbers):
    result = 0
    resultList = []

    for index1 in range(len(numbers)):

        pair = 2020 - numbers[index1]

        for index2 in range(len(numbers)):

            if index2 == index1:
                continue
            elif numbers[index2] == pair:
                result = numbers[index1] * numbers[index2]
                resultList.append(result)

    finalResult = set(resultList)
    print('Answer for part one is: {0}'.format(printSets(finalResult)))

partOne(numbers)


