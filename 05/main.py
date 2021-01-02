greatestId = 0
seatList = {}

for line in open('input.txt', 'r'):
    row = int(line[:7].replace('F', '0').replace('B', '1'), 2)
    column = int(line[7:].replace('L', '0').replace('R', '1'), 2)
    seatId = row * 8 + column
    greatestId = max(greatestId, seatId)
    seatList[seatId] = True

print(greatestId)
for seatId in range(greatestId, 0, -1):
    if seatId not in seatList and seatId - 1 in seatList and seatId + 1 in seatList:
        print(seatId)
