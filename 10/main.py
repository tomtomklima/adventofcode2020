lines = [int(line.rstrip()) for line in open('input.txt', 'r')] + [0]

lines.sort()

diff1count = 0
diff3count = 1 # for the built-in joltage adapter

for index, value in enumerate(lines[:-1]):
    diff = lines[index + 1] - value
    if diff == 1:
        diff1count += 1
    elif diff == 3:
        diff3count += 1

print(diff1count * diff3count)
