import functools
import operator

def parseLine(line:str) :
    #  IN : Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
    # OUT : (1, [{'blue': 3, 'red': 4}, {'red': 1, 'green': 2, 'blue': 6}, {'green': 2}])

    id_part, data_part = line.strip('\n').split(':')
    id_val = int(id_part.split(' ')[1])
    sets = [{val.split(' ')[1] : int(val.split(' ')[0]) for val in oneSetAsD} for oneSetAsD in [oneSetasList.strip(' ').split(', ') for oneSetasList in data_part.split(';')]]
    return id_val, sets

def getMaxOfEach(lineData:list) :
    maxR = max([oneSet.get('red', 0) for oneSet in lineData])
    maxG = max([oneSet.get('green', 0) for oneSet in lineData])
    maxB = max([oneSet.get('blue', 0) for oneSet in lineData])

    return (maxR, maxG, maxB)

def parseGames(path:str) -> list:
    result = []
    with open(path, 'r') as file :
        for line in file.readlines() :
            id_val, data = parseLine(line)
            result.append((id_val, getMaxOfEach(data)))
    return result

def getPossibleGammes(games:list, qtt:tuple) -> list:
    return [gameId for gameId, data in games if all([data[i] <= qtt[i] for i in range(3)])]

def getPowerOfGames(games:list) :
    return [functools.reduce(operator.mul, game[1]) for game in games]

path = 'k-input.txt'
parsedGames = parseGames(path)

# possibleGames = getPossibleGammes(parsedGames, (12, 13, 14))
# print(f'result (p1): {sum(possibleGames)} : \n\n{possibleGames}')

gamesPowers = getPowerOfGames(parsedGames)
print(f'result (p2): {sum(gamesPowers)} : \n\n{gamesPowers}')