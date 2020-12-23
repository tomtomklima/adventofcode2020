from collections import Counter

if True:
    f = open('input.txt', 'r')
    content = f.read()
else:
    f = open('test.txt', 'r')
    content = f.read()

groups = content.split('\n\n')

answersAnyoneCount = 0
answersEveryoneCount = 0
for group in groups:
    answers = group.split('\n')
    lettersCount = {}
    
    for answer in answers:
        for letter in answer:
            if letter in lettersCount:
                lettersCount[letter] += 1
            else:
                lettersCount[letter] = 1
    
    answersAnyoneCount += len(lettersCount)
    
    maximumHits = len(answers)
    for key, result in lettersCount.items():
        if result == maximumHits:
            answersEveryoneCount += 1
        

print(answersAnyoneCount)
print(answersEveryoneCount)