WIN = 'win'
CANDIDATE = 'candidate'

def parse(rawData) :

    result = []
    for rawCard in rawData :
        _, numbers = rawCard.replace('\n', '').replace('  ', ' ').split(':')
        matcher = r'^Card\s+\d+:((\s+\d+)+)\s\|((\s+(\d+))+)$'
        print(numbers)




def solveP1(rawData) :
    parse(rawData)







path = 'kinput.txt'
with open(path, 'r') as file :
    rawData = file.readlines()

solveP1(rawData)