# Autor Harduin_Hero
# Advent of Code 2025 (https://adventofcode.com/)
# Puzzle 03

from main_part1 import get_filecontent

def find_largest_pos2(pack:list[int], place_value:int, last_largest_pos:int) -> int :
    if place_value < 0 or place_value > 11 :
        raise ValueError("place Value must be in [0;11] !")
    # searching for first digit
    if place_value == 11 : 
        largest_pos = 0
        end = len(pack) - place_value
        largest = pack[0]
    # searching for other digits
    else : 
        largest_pos = last_largest_pos+1
        end = len(pack) - place_value
        largest = pack[last_largest_pos+1]

    for i in range(largest_pos, end) :
        if pack[i] == 9 :
            return i
        if pack[i] > largest :
            largest = pack[i] 
            largest_pos = i
    return largest_pos


def main_p2(target:str) -> int :
    output = 0
    pack_list = [[int(digit) for digit in pack if digit.isdigit()] for pack in get_filecontent(target)]
    for pack in pack_list :
        digits_pos = []
        last_largest_pos = 0
        for place_value in range(12) :
            last_largest_pos = find_largest_pos2(pack, 11-place_value, last_largest_pos)
            digits_pos.append(last_largest_pos)

        joltage = int(''.join([str(pack[pos]) for pos in digits_pos]))
        output += joltage

        print(f"{''.join([str(p) for p in pack])} joltage is {joltage}")
    return output


if __name__ == "__main__" :

    target = "src/input_ex1.txt"
    target = "src/input.txt"

    out = main_p2(target)
    print(out)
