from math import ceil

path = 'knownInput.txt'
path = 'p2-kInput.txt'
path = 'input.txt'

words = {
    'one'   : 1,
    'two'   : 2,
    'three' : 3,
    'four'  : 4,
    'five'  : 5,
    'six'   : 6,  
    'seven' : 7,
    'eight' : 8,
    'nine'  : 9
}

starters = {k[0] : list(len(w)-1 for w in words if w[0] == k[0]) for k in words}

print(words)
print(starters)


def findVal(line:str) -> int :
    digits = [l for l in line if str.isdigit(l)]
    return int(digits[0] + digits[-1]) if digits else 0

def findVal2(line:str) -> int :
    print(line.strip('\n'))
    digits = []
    i = 0
    while i < len(line) :
        l = line[i]

        if str.isdigit(l) :
            digits.append(int(l))
            i += 1
        else :
            # elimine les caracters qui ne sont pas des débuts
            if l not in starters :
                i += 1
                continue
            for jumps in starters[l] :
                if i+jumps+1 <= len(line) and line[i:i+jumps+1] in words :
                    #print(line[i:i+jumps+1])
                    digits.append(words[line[i:i+jumps+1]])
                    i += jumps-1
                    break      
            i+=1
    print(digits)
    return digits[0]*10 + digits[-1]

with open(path, 'r') as file :
    line = file.readline()
    sum = 0
    while line :
        v = findVal2(line)
        sum += v
        line = file.readline()

print(sum)