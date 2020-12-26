import copy

class Map:
    map = []
    stabilized = False
    maxWidthIndex = 0
    maxHeightIndex = 0
    
    
    def __init__(self, map):
        self.map = map
        self.maxWidthIndex = len(map[0]) - 1
        self.maxHeightIndex = len(map) - 1
    
    
    def getOccupiedSeatsCount(self):
        count = 0
        for row in self.map:
            count += row.count('#')
        
        return count
    
    
    def doStep(self):
        self.stabilized = True
        
        newMap = copy.deepcopy(self.map)
        
        for indexRow, row in enumerate(self.map):
            for indexSeat, seat in enumerate(row):
                if seat == '.':  # floor
                    pass
                elif seat == 'L':  # empty
                    # if self.getAnjacentOccupiedSeatsCount(indexSeat, indexRow) == 0:
                    if self.getDirectionalOccupiedSeatsCount(indexSeat, indexRow) == 0:
                        newMap[indexRow][indexSeat] = '#'
                        self.stabilized = False
                    else:
                        newMap[indexRow][indexSeat] = 'L'
                elif seat == '#':  # occupied
                    # if self.getAnjacentOccupiedSeatsCount(indexSeat, indexRow) >= 4:
                    if self.getDirectionalOccupiedSeatsCount(indexSeat, indexRow) >= 5:
                        newMap[indexRow][indexSeat] = 'L'
                        self.stabilized = False
                    else:
                        newMap[indexRow][indexSeat] = '#'
        
        self.map = newMap
    
    
    def getAnjacentOccupiedSeatsCount(self, indexRow, indexSeat):
        indexes = [
            [-1, -1],
            [-1, 0],
            [-1, 1],
            [0, -1],
            [0, 1],
            [1, -1],
            [1, 0],
            [1, 1],
        ]
        
        count = 0
        for x, y in indexes:
            xIndex = x + indexRow
            yIndex = y + indexSeat
            if xIndex < 0 or self.maxWidthIndex < xIndex or yIndex < 0 or self.maxHeightIndex < yIndex:
                pass
            else:
                if self.map[yIndex][xIndex] == '#':
                    count += 1
        
        return count
    
    
    def getDirectionalOccupiedSeatsCount(self, indexRow, indexSeat):
        indexes = [
            [-1, -1],
            [-1, 0],
            [-1, 1],
            [0, -1],
            [0, 1],
            [1, -1],
            [1, 0],
            [1, 1],
        ]
        
        count = 0
        for x, y in indexes:
            xIndex = x + indexRow
            yIndex = y + indexSeat
            while 0 <= xIndex and xIndex <= self.maxWidthIndex and 0 <= yIndex and yIndex <= self.maxHeightIndex:
                if self.map[yIndex][xIndex] == '#':
                    count += 1
                    break
                elif self.map[yIndex][xIndex] == 'L':
                    break
                # else '.' as floor, continue
                
                xIndex += x
                yIndex += y
        
        return count
    
    
    def printMap(self):
        for row in self.map:
            print(*row, sep="")
        
        print('\n')


map = Map([list(line.rstrip()) for line in open('input.txt', 'r')])

while map.stabilized == False:
    map.doStep()
    # map.printMap()

print(map.getOccupiedSeatsCount())
