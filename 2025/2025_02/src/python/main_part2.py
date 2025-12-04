# Autor Harduin_Hero
# Advent of Code 2025 (https://adventofcode.com/)
# Puzzle 02

from main_part1 import get_filecontent

factors = {i:[j for j in range(1,i) if i%j==0 and j<=i/2] for i in range(1,15)}

def get_range2(start:int, end:int) -> list[str]:
    return [str(x) for x in range(start, end+1)]

def is_id_invalid2(id:str) -> bool :
    for factor in factors[len(id)] :
        sub_strings_list = [id[i:i+factor] for i in range(0, len(id), factor)]
        if all([sub_strings_list[0]==sub_strings for sub_strings in sub_strings_list]) :
            return True
    return False

def main_p2(target:str) -> int :
    input_data = [(int(id_range.split('-')[0]),int(id_range.split('-')[1])) for id_range in get_filecontent(target)[0].split(",")]
    output = 0

    for start, end in input_data :

        R = get_range2(start, end)
        invalid_id_list = [int(I) for I in R if is_id_invalid2(I)]
        output += sum(invalid_id_list)

        #print(f"{start}-{end} : {invalid_id_list}")

    return output
    
if __name__ == "__main__" :

    target = "src/input_ex1.txt"
    target = "src/input.txt"

    out = main_p2(target)
    print(out)