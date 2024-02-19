def get_mapper(rawData) :
    mapper = []
    current_state = -1
    for i in range(2, len(rawData)) :
        line = rawData[i].replace('\n', '')
        if line == '' : 
            continue
        splited = line.split(' ')
        if 'map:' in splited :
            mapper.append([])
        else :
            mapper[-1].append([int(e) for e in line.split(' ')])
    return mapper

def solveP1(rawData) :
    mapper = get_mapper(rawData)
    states = [[int(element) for element in rawData[0].split(' ')[1::]]]
    # print(states[-1])
    state = 0
    for converter in mapper :
        states.append(states[-1][::])
        for entry in converter :
            for i in range(len(states[0])) :
                if entry[1] <= states[state][i] < entry[1] + entry[2] :
                    # print(f'{i} : {states[state][i]} - {entry[1]} + {entry[0]} = {states[state][i] - entry[1] + entry[0]}')
                    states[state+1][i] = states[state][i] - entry[1] + entry[0]
        # print(states[state])
        state += 1

    # print(mapper, len(mapper))
    # print(states, len(states))
    return states[-1]

def solveP1(rawData) :
    mapper = get_mapper(rawData)
    seedLine = [int(element) for element in rawData[0].split(' ')[1::]]
    states = []
    for i in range(0, len(seedLine), 2) :
        for j in range(seedLine[i+1]) :
            states.append(seedLine[i]+j)
    print(states)
    states = [states]
    # print(states[-1])
    state = 0
    for converter in mapper :
        states.append(states[-1][::])
        for entry in converter :
            for i in range(len(states[0])) :
                if entry[1] <= states[state][i] < entry[1] + entry[2] :
                    # print(f'{i} : {states[state][i]} - {entry[1]} + {entry[0]} = {states[state][i] - entry[1] + entry[0]}')
                    states[state+1][i] = states[state][i] - entry[1] + entry[0]
        # print(states[state])
        state += 1

    # print(mapper, len(mapper))
    # print(states, len(states))
    return states[-1]


path = 'kinput.txt'
with open(path, 'r') as file :
    rawData = file.readlines()


print('part1 : ', min(solveP1(rawData)))