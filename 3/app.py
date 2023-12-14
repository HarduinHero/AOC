def printM(matrix) :
    for l in matrix :
        print(l, len(l))

def raw2matrix(rawLines) :

    matrix = []
    symbolesPos = []

    for y, line in enumerate(rawLines) :
        tripedLineline = line.strip('\n')
        correctedSplitedLine = []
        x = 0
        while x < len(tripedLineline) :
            cell = tripedLineline[x]

            if str.isdigit(cell) :
                j = x
                cellVal = ''
                #print(tripedLineline)
                while j<len(tripedLineline) and str.isdigit(tripedLineline[j]) :
                    cellVal += tripedLineline[j]
                    j += 1
                jump = j - x
                for _ in range(jump) :
                    correctedSplitedLine.append(int(cellVal))
                x += jump
            else :
                correctedSplitedLine.append(cell)
                if cell != '.' :
                    symbolesPos.append((x, y))
                x += 1

        matrix.append(correctedSplitedLine)
    return matrix, symbolesPos

generalLookup = [
    (-1, -1), (0, -1), (1, -1),
    (-1,  0),          (1,  0),
    (-1,  1), (0,  1), (1,  1),    
]
lookupTable = {

    # x==0,   y==0,   x==max, y==max
    # Nominal case
    ( False, False, False, False) : generalLookup,
    # Corners
    ( True,  True,  False, False) : [generalLookup[i] for i in (4,6,7)], # x0 y0
    ( True,  False, False, True ) : [generalLookup[i] for i in (1,2,4)], # x0 ym
    ( False, True,  True,  False) : [generalLookup[i] for i in (3,5,6)], # xm y0
    ( False, False, True,  True ) : [generalLookup[i] for i in (0,1,3)], # xm ym
    # Sides
    ( True,  False, False, False) : [generalLookup[i] for i in (1,2,4,6,7)], # x0 y?
    ( False, True,  False, False) : [generalLookup[i] for i in (3,4,5,6,7)], # x? y0
    ( False, False, True,  False) : [generalLookup[i] for i in (0,1,3,5,6)], # xm y?
    ( False, False, False, True ) : [generalLookup[i] for i in (0,1,2,3,4)], # x? ym
}

def getPieces(matrix, symboles) :
    result = []

    for pos in symboles :
        nums = set()
        x, y = pos
        print(pos, ' -> ', end='')
        for checkPos in lookupTable[(x==0, y==0, x==max, y==max)] :
            cell = matrix[y+checkPos[1]][x+checkPos[0]]
            print(cell, end=' ')
            if isinstance(cell, int) :
                nums.add(cell)
        result.extend(nums)
        print()
    return result

def getGears(matrix, symboles) :
    result = []

    for pos in symboles :
        nums = set()
        x, y = pos

        if (matrix[y][x] != '*') :
            continue

        print(pos, ' -> ', end='')
        for checkPos in lookupTable[(x==0, y==0, x==max, y==max)] :
            cell = matrix[y+checkPos[1]][x+checkPos[0]]
            print(cell, end=' ')
            if isinstance(cell, int) :
                nums.add(cell)

        if len(nums) == 2 :
            result.append(tuple(nums))

        print()
    return result

path = 'input.txt'
with open(path, 'r') as file :
    rawLines = file.readlines()

matrixed, symboles = raw2matrix(rawLines)
printM(matrixed)
print(symboles)
print()

# p1
# pieces = getPieces(matrixed, symboles)
# print()
# print(pieces)
# print(sum(pieces))
# 532428

# p2
gears = getGears(matrixed, symboles)
print()
print(gears)
print(sum([g[0]*g[1] for g in gears]))
# 84051670