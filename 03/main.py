def isTreeInPosition(row, positon):
    modulatedPositon = positon % len(row)
    return row[modulatedPositon] == '#'

f = open('input.txt', 'r')
rows = [line.rstrip() for line in f]

treesCount = 0

for i, row in enumerate(rows):
   if isTreeInPosition(row, i * 3):
       treesCount += 1

print(treesCount)

slopes = [
    [1, 1],
    [3, 1],
    [5, 1],
    [7, 1],
    [1, 2],
]

treesMultiple = 1

for x, y in slopes:
    treesCount = 0
    rowChecked = 0
    for i, row in enumerate(rows):
        if i % y == 0:
            if isTreeInPosition(row, rowChecked * x):
                treesCount += 1
            rowChecked += 1
    
    treesMultiple *= treesCount

print(treesMultiple)
