from math import sqrt, ceil, floor

kTime = [7, 15, 30]
kRecord = [9, 40, 200]
kResp = [4, 8,  9]

Time = [55, 82, 64, 90]
Record = [246, 1441, 1012, 1111]

def natural_rounding(x) :
    x1 = ceil(x)
    x2 = floor(x)
    if x - x1 > x - x2 :
        return x2
    return x1

def solveP1(T, R) :
    # On cherle les solutions de x(T-x)-R = 0 ou -x²+xT-R = 0 : ax²+bx+c
    # x le temps d'appuis
    # T le temps max de la course
    # R le record à batre
    a = -1
    b = T
    c = -R
    delta = natural_rounding(b**2 - 4*a*c) # b²-4ac
    if delta > 0 :
        x1 = natural_rounding((-b-sqrt(delta)) / (2*a))
        x2 = natural_rounding((-b+sqrt(delta)) / (2*a))
        count = 0
        for x in range(x2, x1) :
            #print(x, ' ', -x**2+x*T-R)
            if -x**2+x*T-R > 0 :
                count+=1
        return count
    elif delta == 0 :
        return 1
    else :
        return 0

print('############# Solve 1 #############')
total = 1
for T, R in zip(Time, Record) :
    r = solveP1(T, R)
    total*=r
    print(f'Pour T={T} et R={R}, on trouve {r}')
print (f'on a au finale : {total}')

print('############# Solve 2 #############')
T = int(''.join([str(e) for e in Time]))
R = int(''.join([str(e) for e in Record]))

r = solveP1(T, R)
print(f'Pour T={T} et R={R}, on trouve {r}')