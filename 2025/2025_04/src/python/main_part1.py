# Autor Harduin_Hero
# Advent of Code 2025 (https://adventofcode.com/)
# Puzzle 04

def get_filecontent(filename:str) -> list[str] :
    with open(filename, "r") as file :
        output = file.readlines()
    return output

def main_p1(target:str) -> int :
    input_data = get_filecontent(target)
    return 0
    
if __name__ == "__main__" :

    #target = "src/input_ex1.txt"
    target = "src/input.txt"

    out = main_p1(target)
    print(out)
