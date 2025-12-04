# Autor Harduin_Hero
# Advent of Code 2025 (https://adventofcode.com/)
# Puzzle 02

def get_filecontent(filename:str) -> list[str] :
    with open(filename, "r") as file :
        output = file.readlines()
    return output

def get_range(start:int, end:int) -> list[str]:
    return [str(x) for x in range(start, end+1) if len(str(x))%2==0]

def is_id_invalid(id:str) -> bool :
    return id[:len(id)//2] == id[len(id)//2:]

def main_p1(target:str) -> int :
    input_data = [(int(id_range.split('-')[0]),int(id_range.split('-')[1])) for id_range in get_filecontent(target)[0].split(",")]
    output = 0

    for start, end in input_data :
        R = get_range(start, end)
        invalid_id_list = [int(I) for I in R if is_id_invalid(I)]
        output += sum(invalid_id_list)
        print(f"{start}-{end} : {invalid_id_list}")
    return output
    
if __name__ == "__main__" :
    #target = "src/input_ex1.txt"
    target = "src/input.txt"

    out = main_p1(target)

    print(out)