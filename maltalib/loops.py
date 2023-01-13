from maltalib.conditions import ifs
import maltalib.variables
#import maltalib.conditions
import sys

def goto(stamp, line, stamplist, stampline_list):
    stamp = stamp.replace(" ", "")
    stamp = stamplist.index(stamp)
    goto.line = stampline_list[stamp]
    return goto.line

def while_loop(readline, allvarlist, all_valuelist, stamplist, stampline_list, line):
    while_loop.line = 0
    f = open(sys.argv[1], 'r')
    read = f.readlines()
    readline = readline.replace("while", "")
    maltalib.conditions.ifs(readline, allvarlist, all_valuelist, stamplist, stampline_list, line)
    line = maltalib.conditions.ifs.line
    readline2 = readline
    
    while maltalib.conditions.ifs.true == True: #continue
        maltalib.conditions.ifs(readline2, allvarlist, all_valuelist, stamplist, stampline_list, line)

        line += 1
        if line == maltalib.conditions.ifs.endline:
            line = maltalib.conditions.ifs.line 

        if line < len(read):
            readline = read[line + 1]
        else:
            break

        while readline[:1] == "\t":
            readline = readline[1:]

        while readline[:1] == " ":
            readline = readline[1:]

        readline = readline.replace("\n","")

        if readline[:3] == "mem":
            print(allvarlist)
            print(all_valuelist)

        if readline[:2] == "if":
            readline = readline.replace("if", "")
            maltalib.conditions.ifs(readline, allvarlist, all_valuelist, stamplist, stampline_list, line)
            line = maltalib.conditions.ifs.line

        if readline[:4] == "calc":
            readline = readline.replace("calc", "")
            readline = readline.replace(":", "")
            maltalib.operations.calculator(readline, allvarlist, all_valuelist)

        if readline[:2] == ">>":
            readline = readline.replace(">>", "")
            maltalib.prints.println(readline, allvarlist, all_valuelist)
            if '""' in readline:
                readline = readline.replace
                string = readline

        if readline[:1] == ">" and readline[1] != '>':
            readline = readline.replace(">", "")
            maltalib.prints.printf(readline, allvarlist, all_valuelist)
            if '""' in readline:
                readline = readline.replace
                string = readline

        if readline[:1] == "<":
            readline = readline.replace("<", "")
            maltalib.variables.create_var(readline, allvarlist, all_valuelist)
            
        if readline[:1] == "$":
            readline = readline.replace("$", "")
            maltalib.variables.input_var(readline, allvarlist, all_valuelist)

        if readline[:4] == "goto":
            readline = readline.replace("goto", "")
            maltalib.loops.goto(readline, line, stamplist, stampline_list)
            line = maltalib.loops.goto.line
            
        if readline[:1] == "@":
            readline = readline.replace("@", "")
            maltalib.variables.copy_var(readline, allvarlist, all_valuelist)
            
        if readline[:3] == "del":
            readline = readline.replace("del", "")
            readline = readline.replace(" ", "")
            maltalib.variables.delete_var(readline, allvarlist, all_valuelist)

        if readline[-2:] == "++":
            readline = readline.replace('++','')
            maltalib.operations.increment(readline, allvarlist, all_valuelist)

        
        if readline[-2:] == "--":
            readline = readline.replace('--','')
            maltalib.operations.decrement(readline, allvarlist, all_valuelist)

    else:
        while_loop.line = maltalib.conditions.ifs.endline
        return while_loop.line

        
