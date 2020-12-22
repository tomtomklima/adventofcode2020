def isValid(min, max, char, password):
    count = password.count(char)
    return min <= count & count <= max

def isValidNew(positions, char, password):
    sameLetterCount = 0
    for position in positions:
        if password[int(position) - 1] == char:
            sameLetterCount += 1
    
    return sameLetterCount == 1
    

f = open('input.txt', 'r')
records = [line.rstrip() for line in f]

validPasswordCount = 0
newValidPasswordCount = 0
for record in records:
    rule, password = record.split(': ')
    minmax, char = rule.split(' ')
    min, max = [int(i) for i in minmax.split('-')]
    if isValid(min, max, char, password):
        validPasswordCount += 1
    
    if isValidNew([min, max], char, password):
        newValidPasswordCount += 1

print(validPasswordCount)
print(newValidPasswordCount)
