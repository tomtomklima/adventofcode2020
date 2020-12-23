import itertools


def isNumberSumOfTwoInArray(numbers, wantedNumber):
    for combination in itertools.combinations(numbers, 2):
        if combination[0] + combination[1] == wantedNumber:
            return True
    
    return False


def getProblematicNumber(allNumbers):
    count = 1
    numbers = []
    for newNumber in allNumbers:
        if (count > 25):
            count -= 1
            if not isNumberSumOfTwoInArray(numbers, newNumber):
                return newNumber
            
            numbers.pop(0)
        
        numbers.append(newNumber)
        count += 1


def getSumMinMaxSumsOfNumber(allNumbers, wantedNumber):
    while True:
        sum = 0
        for index, newNumber in enumerate(allNumbers):
            sum += newNumber
            if sum == wantedNumber:
                correctNumbers = allNumbers[0:index+1]
                
                return min(correctNumbers) + max(correctNumbers)
            elif sum > wantedNumber:
                allNumbers.pop(0)
                break


allNumbers = [int(line.rstrip()) for line in open('input.txt', 'r').readlines()]

wantedNumber = getProblematicNumber(allNumbers)
print(wantedNumber)

print(getSumMinMaxSumsOfNumber(allNumbers, wantedNumber))
