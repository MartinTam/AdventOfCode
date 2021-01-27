file = open('input.txt', 'r')

numbersSTR = file.readlines()

numbers = []

for x in numbersSTR:
    numbers.append( int(x) )


def findTwoNumbers(listOfNumbers, sum, exceptIndex = -1):

    twoNumbers = []

    for indexFirstNumber in range( len( listOfNumbers ) ):

        if exceptIndex == indexFirstNumber:
            pass
        else:

            pair = sum - listOfNumbers[indexFirstNumber]

            for indexSecondNumber in range( len( listOfNumbers ) ):

                if ( indexFirstNumber == indexSecondNumber ) or ( indexSecondNumber == exceptIndex ):
                    pass
                else:
                    if listOfNumbers[indexSecondNumber] == pair:
                        twoNumbers.append( listOfNumbers[ indexFirstNumber ] )
                        twoNumbers.append( listOfNumbers[ indexSecondNumber ] )
    
    reduceTwoNumbers = list( set( twoNumbers ) )
    
    if len( reduceTwoNumbers ) == 2:
        return reduceTwoNumbers[0] * reduceTwoNumbers[1]
    else:
        return 0


def findThreeNumbers(listOfNumbers, sum):

    listOfResult = []

    for index in range( len( listOfNumbers ) ):

        sumForAnotherTwo = sum - listOfNumbers[index]
        anotherTwoMultiplied = findTwoNumbers(listOfNumbers, sumForAnotherTwo, index)

        if anotherTwoMultiplied == 0:
            pass
        else:
            listOfResult.append(anotherTwoMultiplied * listOfNumbers[index])
    
    result = list ( set ( listOfResult ) )
    
    if len( result ) == 1:
        return result[0]
    else:
        return 0

print( 'Part one: {0}'.format( findTwoNumbers(numbers, 2020) ) )
print( 'Part two: {0}'.format( findThreeNumbers(numbers, 2020) ) )
