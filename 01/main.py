def getEqualFromArray(numbersArray, depth, desiredNumber):
    if depth == 1:
        for num in numbersArray:
            if desiredNumber == num:
                return num
    else:
        for num in numbersArray:
            result = getEqualFromArray(numbersArray, depth - 1, desiredNumber - num)
            if (result is not None):
                return num * result


f = open('input.txt', 'r')
numbersArray = [int(line.rstrip()) for line in f]
print(getEqualFromArray(numbersArray, 2, 2020))
print(getEqualFromArray(numbersArray, 3, 2020))
