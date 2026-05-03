# Autor Harduin_Hero
# Advent of Code 2025 (https://adventofcode.com/)
# Puzzle 04

from main_part1 import get_filecontent, print_grid, get_adjacent

def main_p2(target:str) -> int:
    output = 0
    current_grid = [[c for c in line.replace('\n','')] for line in get_filecontent(target)]
    print("Initial state:")
    print_grid(current_grid)

    while True :
        next_grid = [[c for c in l] for l in current_grid]
        removable_rolls = 0
        
        for y in range(len(current_grid)) :
            for x in range(len(current_grid[0])) :
                if current_grid[y][x] != '@' :
                    continue
                adj = get_adjacent(current_grid, y, x)
                if adj.count("@") < 5 :
                    removable_rolls += 1
                    next_grid[y][x] = "X"
        
        output += removable_rolls
        if removable_rolls == 0 :
            break
        print(f"Remove {removable_rolls} rolls of paper:")
        print_grid(next_grid)
        current_grid = [['@' if c=='@' else '.' for c in l] for l in next_grid]

    return output

if __name__ == "__main__" :

    target = "src/input_ex1.txt"
    target = "src/input.txt"

    out = main_p2(target)
    print(out)
