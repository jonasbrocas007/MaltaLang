import maltalib.prints
import maltalib.variables
import maltalib.loops
import maltalib.operations
import maltalib.conditions
import maltalib.garbage_collector
import maltalib.functions
def call_function(readline, function_list, return_list, read, allvarlist, all_valuelist):
    function_called = function_list.get(readline)
    return_called = return_list.get(readline)

    for i in range(function_called + 1, return_called):
        readline = read[i]
        readline = readline.replace("{","")
        readline = readline.replace("}","")

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
            maltalib.functions.call_function(readline, function_list, return_list, read)
            
'''
;function

{x++}
{<b = 0 i}
{@ b,x}

return function

'''