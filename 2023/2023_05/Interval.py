class Intervale :
    def __init__(self, bornes=(None, None)) :
        self.start, self.end = bornes
        if self.end == None or self.start == None :
            self.start = None
            self.end = None
        elif self.start > self.end :
            raise ValueError(f'{self.start} > {self.end} le début d\'un intervale doit etre plus petit que sa fin')

    def __bool__(self) :
        return not(self.isEmpty())
    
    def copy(self) :
        return Intervale(self.getTuple())
    
    def isEmpty(self) :
        return self.start == None and self.end == None

    def __eq__(self, other) -> bool:
        return self.start == other.start and self.end == other.end
    
    def __str__(self) -> str:
        return repr(self.getTuple())
    
    def getTuple(self) :
        return (self.start, self.end)
    
    def getRange(self) :
        return range(self.start, self.end+1)
    
    def size(self) :
        return self.end - self.start +1
    
    def overlaps(self, other) :
        return not(self.start > other.end or self.end < other.start)
    
    def intersection(self, other) :
        if not(self.overlaps(other)) :
            return Intervale()
        return Intervale((
            max(self.start, other.start),
            min(self.end, other.end)
        ))

    def sub(self, other) :
        if not(self.overlaps(other)) :
            return self.copy(),
        
        minStart = min(self.start, other.start)
        maxEnd   = max(self.end  , other.end  )

        if minStart == other.start and maxEnd == other.end :
            return Intervale(),

        elif minStart == self.start and maxEnd == self.end :
            result = []
            if self.start != other.start :
                result.append(Intervale((self.start, other.start-1)))
            if self.end != other.end :
                result.append(Intervale((other.end+1, self.end)))
            return tuple(result)

        elif minStart == self.start and maxEnd == other.end :
            return Intervale((self.start, other.start-1)),
        elif minStart == other.start and maxEnd == self.end :
            return Intervale((other.end+1, self.end)),
        else :
            raise Exception(f'{self}-{other} Normaly unreachable')

# a = Intervale((5,9))
# b = Intervale((1,3))
# c = Intervale((10,30))
# d = Intervale((3,7))
# e = Intervale((9,10))
# f = Intervale((2,10))
# print(f'a overlaps b = {a.overlaps(b)}')
# print(f'a overlaps c = {a.overlaps(c)}')
# print(f'a overlaps d = {a.overlaps(d)}')
# print(f'a overlaps e = {a.overlaps(e)}')
# print(f'a overlaps f = {a.overlaps(f)}')
# print('')
# print(f'a inter b = {a.intersection(b)}')
# print(f'a inter c = {a.intersection(c)}')
# print(f'a inter d = {a.intersection(d)}')
# print(f'a inter e = {a.intersection(e)}')
# print(f'a inter f = {a.intersection(f)}')
# print('')
# print(f'a - b = {a.sub(b)}')
# print(f'a - c = {a.sub(c)}')
# print(f'a - d = {a.sub(d)}')
# print(f'a - e = {a.sub(e)}')
# print(f'a - f = {a.sub(f)}')
# print(f'd - a = {d.sub(a)}')