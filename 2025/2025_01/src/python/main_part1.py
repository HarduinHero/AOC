# Autor : Harduin_Hero
# Advent of Code 2025 (https://adventofcode.com/)
# Puzzle 01

def get_filecontent(filename:str) -> list[str] :
    with open(filename, "r") as file :
        output = file.readlines()
    return output

def rot2int(rotation:str) -> int:
    return int(rotation[1:]) if rotation[0].lower()=='r' else -int(rotation[1:])

def main_p1(target:str) -> int:
    dial_pos = 50
    output   = 0

    instruction_list = get_filecontent(target)
    for instruction in instruction_list :
        old_dial_pos = dial_pos
        change = rot2int(instruction)

        dial_pos = (dial_pos + change) % 100

        print(f"{old_dial_pos}\t-->\t{dial_pos}\tby {instruction[:-1]}({change})\t", end=" ")
        if dial_pos == 0 :
            print("+1")
            output += 1
        else :
            print()

    return output

if __name__ == "__main__" :

    #target = "../input_ex1.txt"
    target = "../input_1.txt"

    out = main_p1(target)
    print(out)