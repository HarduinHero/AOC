# Autor Harduin_Hero
# Advent of Code 2025 (https://adventofcode.com/)
# Puzzle 03

def get_filecontent(filename:str) -> list[str] :
    with open(filename, "r") as file :
        output = file.readlines()
    return output

def find_largest_pos(pack:list[int], first_largest_pos:int|None=None) -> int :
    # searching for first digit
    if first_largest_pos is None : 
        largest_pos = 0
        end = len(pack)-1
        largest = pack[0]
    # searching for second digit
    else : 
        largest_pos = first_largest_pos+1
        end = len(pack)
        largest = pack[first_largest_pos+1]
    for i in range(largest_pos, end) :
        if pack[i] == 9 :
            return i
        if pack[i] > largest :
            largest = pack[i] 
            largest_pos = i
    return largest_pos


def main_p1(target:str) -> int :
    output = 0
    pack_list = [[int(digit) for digit in pack if digit.isdigit()] for pack in get_filecontent(target)]
    for pack in pack_list :
        first_largest_pos  = find_largest_pos(pack)
        second_largest_pos = find_largest_pos(pack, first_largest_pos)
        joltage = int(str(pack[first_largest_pos]) + str(pack[second_largest_pos]))
        output += joltage

        print(f"{''.join([str(p) for p in pack])} joltage is {joltage}")
    return output
    
if __name__ == "__main__" :

    target = "src/input_ex1.txt"
    target = "src/input.txt"

    out = main_p1(target)
    print(out)
