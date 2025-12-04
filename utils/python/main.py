from datetime import datetime
from pathlib import Path
from __main__ import __file__

#############################################
#####            FILE CONTENT           #####  
#############################################
MAIN_PART1_CONTENT = """# Autor Harduin_Hero
# Advent of Code {year} (https://adventofcode.com/)
# Puzzle {day:02d}

def get_filecontent(filename:str) -> list[str] :
    with open(filename, "r") as file :
        output = file.readlines()
    return output

def main_p1(target:str) -> int :
    input_data = get_filecontent(target)
    return 0
    
if __name__ == "__main__" :

    #target = "src/input_ex.txt"
    target = "src/input.txt"

    out = main_p1(target)
    print(out)
"""
MAIN_PART2_CONTENT = """# Autor Harduin_Hero
# Advent of Code {year} (https://adventofcode.com/)
# Puzzle {day:02d}

from main_part1 import get_filecontent

def main_p2(target:str) -> int:
    input_data = get_filecontent(target)
    return 0

if __name__ == "__main__" :

    #target = "src/input_ex.txt"
    target = "src/input.txt"

    out = main_p2(target)
    print(out)
"""
README = """= AoC {year} - Jour {day:02d} : <Titre>
:autor: Harduin_Hero
:toc: left
:toc-title: Sommaire
:stem: latexmath
:source-highlighter: pygments
:imagesdir: img

link:../README.adoc[HOME]

Ceci est un rapport sur ma solution au puzzle **{day:02d}** de l'https://adventofcode.com[Advent Of Code {year}].

== Partie 1
== Partie 2
"""
INDEX_TABLE_LINE = "|{day:02d} |Titre |``_ _`` |link:{workdirname}/README.adoc[Voir]"

#############################################
#####               HELPER              #####  
#############################################

def yes_no_question(Q:str, default_yes:bool=False, default_no:bool=False) -> bool :
    if default_yes and default_no :
        raise ValueError("Only one answer can be the default you dumass.")
    suffix = f"({'Y' if default_yes else 'y'}/{'N' if default_no else 'n'}) > "
    output = None
    while output == None :
        response = input(f"{Q} {suffix}").lower()
        if response == "" and (default_yes or default_no) :
            output = default_yes
        elif response == "y" or response == "n" :
            output = response == "y"
    return output
        
def int_question(Q:str, default:int|None=None, min_boundary:int|None=None, max_boundary:int|None=None) -> int :
    if default is not None and (\
       (min_boundary is not None and default < min_boundary) or\
       (max_boundary is not None and default > max_boundary)) :
        raise ValueError("Default value must be in set boundaries stupid.")
    suffix = ""
    if min_boundary is not None and max_boundary is not None :
        suffix = f"[{min_boundary};{max_boundary}] "
    elif min_boundary is not None :
        suffix = f"[>={min_boundary}] "
    elif max_boundary is not None :
        suffix = f"[<={max_boundary}] "
    if default is not None :
        suffix += f"({default}) > "
    else :
        suffix += f"> "
    output = None
    while output == None :
        response = input(f"{Q} {suffix}")
        if response == "" and default is not None :
            output = default
        try:
            int_response = int(response)
        except ValueError :
            continue
        
        if min_boundary is not None and int_response < min_boundary or\
            max_boundary is not None and int_response > max_boundary :
            continue
        else :
            output = int_response
    return output

def create_dir(dir:Path, exist_ok=False) :
    status = f"DIR\t{dir.name}"
    status += "\tEXISTS...." if dir.exists() else "\t.........."
    try :
        dir.mkdir()
    except FileExistsError :
        if exist_ok :
            status += "SKIP"
        else :
            raise FileExistsError(status + "ERROR")
    else :
        status += "CREATED"
    print(status)

def create_file(filepath:Path, exist_ok=False, content:str="") :
    status = f"FILE\t{filepath.name}"
    if filepath.exists() :
        status += "\tEXISTS...."
        if exist_ok : 
            status += "SKIP"
        else :
            raise FileExistsError(status + "ERROR")
    else : 
        status += "\t.........."
        with open(filepath, "w") as created_file :
            created_file.write(content)
        status += "CREATED"
    print(status)

#############################################
#####               MAIN                #####  
#############################################

if __name__ == "__main__" :
    print("----- New day initialization (Python) -----")

    ### INIT QUESTIONS ###
    
    ## Date
    today = datetime.today()
    year, day = today.year, today.day
    dirname = f"{year}_{day:02d}"
    if yes_no_question(f"[{dirname}] Use current date ?", default_yes=True) :
        pass
    else :
        year = int_question("From which year is the puzzle ?", default=year, min_boundary=0)
        day  = int_question("Which day ?", default=day, min_boundary=1, max_boundary=25)
        dirname = f"{year}_{day:02d}"

    print()

    ## Location definition and validation
    ADVENT_OF_CODE_REPO_ROOT = (Path(__file__) / Path(f"../../..")).resolve()
    yeardir = ADVENT_OF_CODE_REPO_ROOT / str(year)
    workdir = yeardir / dirname
    srcdir  = workdir / "src"
    src_files = ["input.txt", "input_ex.txt"]
    src_python = srcdir / "python"
    src_python_main1 = src_python / "main_part1.py"
    src_python_main2 = src_python / "main_part2.py"
    imgdir  = workdir / "img"
    readme_path = workdir / "README.adoc"
    print(
        f"Next step will create the folowing topography at this path :\n\n" \
        f"{workdir}\n\n"                    \
        f"{year}\n"                         \
        f" ┗━ {dirname}/\n"                 \
        f"     ┣━ src/\n"                   \
        f"     ┃   ┣━ input.txt\n"          \
        f"     ┃   ┣━ input_ex.txt\n"      \
        f"     ┃   ┗━ python/\n"            \
        f"     ┃       ┣━ main_part1.py\n"  \
        f"     ┃       ┗━ main_part2.py\n"  \
        f"     ┣━ img/\n"                   \
        f"     ┗━ README.adoc"
    )
    if not(yes_no_question("Accept", default_yes=True)) :
        print("-----")
        quit()

    ## Topology creation
    create_dir(yeardir, exist_ok=True)
    create_dir(workdir, exist_ok=True)
    create_dir(srcdir, exist_ok=True)
    for src_file in src_files :
        create_file(srcdir/src_file, exist_ok=True)
    create_dir(imgdir, exist_ok=True)

    context_dict = {"year":year, "day":day,"workdirname":dirname}

    try :
        create_dir(src_python, exist_ok=False)
        create_file(src_python_main1, exist_ok=False, content=MAIN_PART1_CONTENT.format(**context_dict))
        create_file(src_python_main2, exist_ok=False, content=MAIN_PART2_CONTENT.format(**context_dict))
        create_file(readme_path,      exist_ok=False, content=README.format(**context_dict))
    except FileExistsError as e :
        print(e)
        print("-----")
        quit()

    # TABLE INDEX UPDATE
    print(f"Add the folowing line to {ADVENT_OF_CODE_REPO_ROOT / "README.adoc"} :\n")
    print(f"{INDEX_TABLE_LINE.format(**context_dict)}")
    print("\n JOB DONE\n-----")
