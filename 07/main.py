def isContaining(specification, bagSpecificationColor, wantedColor):
    for bagSpecification in specification[bagSpecificationColor]:
        if wantedColor == bagSpecification or isContaining(specification, bagSpecification, wantedColor):
            return True
    
    return False


def howManyBagsIsAbove(specification, wantedColor):
    colorCounter = 0
    for bagSpecificationColor in specification:
        if isContaining(specification, bagSpecificationColor, wantedColor):
            colorCounter += 1
    
    return colorCounter


def howManyBagsIsInWithThisBag(specification, wantedColor):
    bagCount = 1  # this bag
    for bagColor in specification[wantedColor]:
        bagCount += howManyBagsIsInWithThisBag(specification, bagColor) * specification[wantedColor][bagColor]
    
    return bagCount


specification = {}

# for line in open('test.txt', 'r'):
for line in open('input.txt', 'r'):
    color, bagsSpecification = line.split(" bags contain ")
    if not color in specification:
        specification[color] = {}
    if bagsSpecification == "no other bags.\n":
        specification[color] = {}
    else:
        for rawListSpec in bagsSpecification.split(", "):
            number, color1piece, color2piece = rawListSpec.split(" ")[0:3]
            colorName = color1piece + " " + color2piece
            specification[color][colorName] = int(number)

print(howManyBagsIsAbove(specification, 'shiny gold'))
print(howManyBagsIsInWithThisBag(specification, 'shiny gold') - 1)  # we dont want to count the first actual bag
