def solveP1(rawData) :
    result = []
    for rawCard in rawData :
        left, right = rawCard.replace('\n', '').replace('  ', ' ').split(':')[1].split(' | ')
        wining = set(left.split(' ')[1::])
        candidates = set(right.split(' '))
        result.append(len(wining.intersection(candidates)))
    return result

def solveP2(wincounts) :
    cardCount = [1 for _ in range(len(wincounts))]
    for cardIndex in range(len(cardCount)) :
        for i in range(wincounts[cardIndex]) :
            cardCount[cardIndex+i+1] += cardCount[cardIndex]
    return cardCount

path = 'input.txt'
with open(path, 'r') as file :
    rawData = file.readlines()

print(solveP1(rawData))
print(solveP2(solveP1(rawData)))
print('part1 : ', sum([int(2**(i-1)) for i in solveP1(rawData)]))
print('part2 : ', sum(solveP2(solveP1(rawData))))