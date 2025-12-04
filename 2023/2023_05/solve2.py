from typing import *
from Interval import Intervale

def rangeDecomp(r1: Tuple[int, int], r2: Tuple[int, int]) -> Tuple[int, int]:
    """
    retourne inner et outer
    inner : parties de r1 dans r2
    outer : parties de r1 non dans r2
    ou r1 et r2 sont des intervales d'entier définits par leur bornes
    r1 = (a, b)
    r2 = (c, d)

---- AVEC a < b ET c < d --------------------------------------------
              c----------d          
      a----b  |          |           #01 inner = []   outer = [ab]
           a--|--b       |           #02 inner = [cb] outer = [ac]
              |  a----b  |           #03 inner = [ab] outer = []
              |       a--|--b        #04 inner = [ad] outer = [db]
              |          |  a----b   #05 inner = []   outer = [ab]
           a--|----------|--b        #06 inner = [cd] outer = [ac, db]
              |          |
              |          |           ----- CAS DES EGALITEES -----
         a----b          |           #07 inner = [bb] outer = [a b-1]
              |          a----b      #08 inner = [aa] outer = [a+1 b]
              a----------b           #09 inner = [ab] outer = [] |
              a----b     |           #10 inner = [ab] outer = [] |> meme cas 
              |     a----b           #11 inner = [ab] outer = [] |

---- AVEC a = b ET c < d --------------------------------------------
              c----------d           
         a=b  |          |           #12 inner = []   outer = [ab]
             a=b         |           #13 inner = [cb] outer = []
              |    a=b   |           #14 inner = [ab] outer = []
              |         a=b          #15 inner = [ad] outer = []
              |          |  a=b      #16 inner = []   outer = [ab]

---- AVEC a < b ET c = d -------------------------------------------
             c=d
      a----b  |                      #17 inner = []   outer = [ab]
           a--|--b                   #18 inner = [cb] outer = [ac, db]
              |  a----b              #19 inner = []   outer = [ab]
         a----b                      #20 inner = [bb] outer = [a b-1]
              a----b                 #21 inner = [aa] outer = [a+1 b]

---- AVEC a = b ET c = d -------------------------------------------
             c=d
         a=b  |                      #22 inner = []   outer = [ab]
             a=b                     #23 inner = [ab] outer = []
              |  a=b                 #24 inner = []   outer = [ab]
    """
    inner = []
    outer = []
    seed = Intervale(r1)
    sourceIN = Intervale(r2)

    outer = [element.getTuple() for element in list(seed.sub(sourceIN)) if element]
    temp = sourceIN.intersection(seed)
    if temp :
        inner = [temp.getTuple()]

    # if b < c or d < a : #01 #05 #12 #16 #17 #19 #22 #24
    #     inner, outer = [], [(a,b)]
    # elif c <= a and b <= d : #03 #09 #10 #11 #14 #23
    #     inner, outer = [(a,b)], []
    # elif b == c and a < b: #07 #20
    #     inner, outer = [(b,b)], [(a,b-1)]
    # elif a == d and a < b: #08 #21
    #     inner, outer = [(a,a)], [(a+1,b)]
    # elif a < c < b < d : 
    #     inner, outer = [(c,b)], [(a,c)]
    # elif c < a < d < b :
    #     inner, outer = [(a,d)], [(d,b)]
    # elif c < d < a < b :
    #     inner, outer = [], [(a,b)]
    # elif a < c < d < b :
    #     inner, outer = [(c,d)], [(a,c), (d,b)]
    # else :
    #     print(a, b, c, d)
    #     raise Exception('normaly unreachable')

    return inner, outer

def get_mapper(rawData) :
    print('----- lecture des fj -----')
    mapper = []
    for i in range(2, len(rawData)) :
        line = rawData[i].replace('\n', '')
        if line == '' : 
            continue
        splited = [int(element) for element in  line.split(' ') if element.isdigit()]
        if splited == [] :
            mapper.append([])
            print(f'fj où j = {len(mapper)}')
        else :
            alpha = splited[1]
            beta  = splited[1]+splited[2]-1
            K     = splited[0]-splited[1]
            print(f'\t (alpha = {alpha}, beta = {beta}, K = {K})')
            mapper[-1].append((alpha, beta, K))
    return mapper

def solveP2(rawData) :
    f = get_mapper(rawData)
    
    # initialisation des résultats
    print('\n----- lecture des interveles x à j=0 -----')
    y = []
    l1 = [int(element) for element in rawData[0].split(' ')[1::]]
    for i in range(0, len(l1), 2)  :
        a = l1[i]
        b = a + l1[i+1] -1
        y.append((a, b))
        print(f'\t[{a}, {b}]')

    # application
    print('\n----- application des fj -----')
    for j in range(len(f)) :
        print(f'j = {j}')
        x = list(y)
        y = set()
        for l in range(len(f[j])) :
            alpha, beta, Kjl = f[j][l]
            sourceInterval = Intervale((alpha, beta))
            print(f'\tl = {l} : {sourceInterval} | x={x} y={y}')
            reste = set()
            for xi in x :
                inner, outer = rangeDecomp(xi, (alpha, beta))
                
                if outer :
                    reste = reste.union(set(outer))
                if inner :
                    y.add((inner[0][0]+Kjl, inner[0][1]+Kjl))
                print(f'\t\txi={xi}')
                print(f'\t\t\t  OUT : {outer}')
                print(f'\t\t\t   IN : {inner}')
                print(f'\t\t\treste : {reste}')
                print(f'\t\t\t    y : {y}')
            x = list(reste)
        y = y.union(set(x))
    return y

path = 'input.txt'
with open(path, 'r') as file :
    rawData = file.readlines()

print(min([e[0] for e in list(solveP2(rawData))]))