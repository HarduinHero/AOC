# Autor Harduin_Hero
# Advent of Code 2025 (https://adventofcode.com/)
# Puzzle 04

def get_filecontent(filename:str) -> list[str] :
    with open(filename, "r") as file :
        output = file.readlines()
    return output

def print_grid(grid) :
    for l in grid :
        print(''.join(l))

def get_adjacent(grid:list[list[str]], y:int, x:int) -> list[str]:
    y_max, x_max = len(grid)-1, len(grid[0])-1
    coord_to_check = [(y-1,x-1), (y-1,x), (y-1,x+1), (y,x-1), (y,x+1), (y+1,x-1), (y+1,x), (y+1,x+1)]
    coord_to_check = [coord for coord in coord_to_check if coord[0]>=0 and coord[1]>=0 and coord[0]<=y_max and coord[1]<=x_max]
    return [grid[coord[0]][coord[1]] for coord in coord_to_check]

def main_p1(target:str) -> int :
    grid = [[c for c in line.replace('\n','')] for line in get_filecontent(target)]
    debug_grid = [[c for c in l] for l in grid]
    output = 0
    for y in range(len(grid)) :
        for x in range(len(grid[0])) :
            if grid[y][x] != '@' :
                continue
            adj = get_adjacent(grid, y, x)
            #print(f"({y}, {x}) - {adj}")
            if adj.count("@") < 4 :
                output += 1
                debug_grid[y][x] = "X"

    print_grid(debug_grid)
    return output
    
if __name__ == "__main__" :

    target = "src/input_ex1.txt"
    target = "src/input.txt"

    out = main_p1(target)
    print(out)