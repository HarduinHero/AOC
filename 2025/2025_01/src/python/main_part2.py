from main_part1 import get_filecontent, rot2int

def main_p2(target:str) -> int:
    dial_pos = 50
    output   = 0

    instruction_list = get_filecontent(target)
    for instruction in instruction_list :
        old_dial_pos = dial_pos
        change = rot2int(instruction)
        increase = 0

        n_full_turn = abs(change) // 100
        increase += n_full_turn

        dial_pos = (dial_pos + change) % 100
        
        print(f"{old_dial_pos}\t-->\t{dial_pos}\t{change}\tn_full_turn {n_full_turn} times\t", end=" ")

        if dial_pos == 0 :
            increase += 1
        elif old_dial_pos == 0 :
            increase += 0
        elif change > 0 and dial_pos < old_dial_pos :
            increase += 1
        elif change < 0 and dial_pos > old_dial_pos :
            increase += 1

        print(f"+{increase}")
        
        output += increase

        
    return output

if __name__ == "__main__" :

    #target = "../input_ex1.txt"
    #target = "../input_ex2.txt"
    target = "../input_1.txt"

    out = main_p2(target)
    print(out)