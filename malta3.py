if not __name__ == "__main__":
    exit("ERROR: The MAL interpreter should not be run as a library!")

import sys
import threading

#from maltalib import 
import maltalib.prints
import maltalib.variables
import maltalib.loops
import maltalib.operations
import maltalib.conditions
import maltalib.garbage_collector
import maltalib.functions


f = open(sys.argv[1], 'r')


def string_to_list(readline):
    readline = readline.replace('\n', '')
    readline = readline.replace('[', '')
    readline = readline.replace(']', '')
    readline = readline.replace("'", '')
    readline = readline.replace('"', '')


stampline = 0
stamplist = []
stampline_list = []
return_list = {}
function_list = {}

allvarlist = []
all_valuelist = []
read = f.readlines()
line = 0
gb_count = 0


while stampline <= len(read):
    while line < len(read):
        readline = read[line]

        while readline[:1] == "\t":
            readline = readline[1:]

        while readline[:1] == " ":
            readline = readline[1:]

        if readline[:1] == ":":
            readline = readline.replace('\n', '')
            readline = readline.replace(":", "")
            readline = readline.split(" ")
            stamplist.append(readline[0])
            stampline_list.append(line)

        if readline[:1] == ";":
            readline = readline.replace('\n', '')
            readline = readline.replace(";", "")
            readline = readline.split(" ")
            function_list[readline[0]] = line

        if readline[:6] == "return":
            readline = readline.replace('\n', '')
            readline = readline.replace("return", "")
            readline = readline.split(" ")
            return_list[readline[1]] = line

        line += 1
    stampline += 1

line = 0
#print(function_list)
#print(return_list)

while stampline <= len(read):
    while line < len(read):
        readline = read[line]

        if readline[:1] == "return":
            readline = readline.replace('\n', '')
            readline = readline.replace(":", "")
            readline = readline.split(" ")
            stamplist.append(readline[0])
            stampline_list.append(line)

        line += 1
    stampline += 1

line = 0

while line < len(read):
    readline = read[line]
    while readline[:1] == "\t":
        readline = readline[1:]

    while readline[:1] == " ":
        readline = readline[1:]

    readline = readline.replace("\n","")

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
        allvarlist = delete_var.varlist 
        all_valuelist = delete_var.var_valuelist 

    if readline[:4] == "calc":
        readline = readline.replace("calc", "")
        readline = readline.replace(":", "")
        maltalib.operations.calculator(readline, allvarlist, all_valuelist)

    if readline[:3] == "mem":
        print(allvarlist)
        print(all_valuelist)

    if readline[:2] == "if":
        readline = readline.replace("if", "")
        maltalib.conditions.ifs(readline, allvarlist, all_valuelist, stamplist, stampline_list, line)
        line = maltalib.conditions.ifs.line

    if readline[:5] == "while":
        maltalib.loops.while_loop(readline, allvarlist, all_valuelist, stamplist, stampline_list, line)
        if maltalib.loops.while_loop.line != 0: #if the condition is not true, go to the end stamp
            line = maltalib.loops.while_loop.line

    if readline[-2:] == "++":
        readline = readline.replace('++','')
        maltalib.operations.increment(readline, allvarlist, all_valuelist)

    if readline[-2:] == "--":
        readline = readline.replace('--','')
        maltalib.operations.decrement(readline, allvarlist, all_valuelist)

    if readline[:1] == "&": #&x <- x + 1
        readline = readline.replace("&", '')
        maltalib.variables.shift(readline, allvarlist, all_valuelist)

    if readline[:4] == "call":
        readline = readline.replace("call", '')
        readline = readline.replace(" ", '')

        read = [x.replace("\n","") for x in read]
        maltalib.functions.call_function(readline, function_list, return_list, read, allvarlist, all_valuelist)

        

    line += 1
f.close
