if not __name__ == "__main__":
    exit("ERROR: The MAL interpreter should not be run as a library!")
from enum import Enum
import re
import time
#for counting the application runtime
#from datetime import datetime
#start_time = datetime.now()
import sys
f = open(sys.argv[1], 'r')
a = 0
line = 0
allvarlist = []
result = []
rows = []
read = f.readlines()
stamplist = []
number = 0
empty = []
stampline = 0
whilelist = []
number = 0
allfilelist = []
var = 0
len_read_list = []
read_list = []


while stampline <= len(read):
    while line < len(read):
        readline = read[line]
        if readline[0] == ':':
            readstamp = readline.replace('\n', '')
            readstamp = readstamp.replace(',', '')
            readstamp = readstamp.replace('[', '')
            readstamp = readstamp.replace(']', '')
            readstamp = readstamp.replace("'", '')
            readstamp = readstamp.replace(":", '')
            readstamp = readstamp.split(' ')
            stamplist.append(readstamp[0])
            stamplist.append(line)
        line += 1
    stampline += 1 
    
readst = str(read)
if 'END' not in readst:
    print('Error, you need to end the program with the END keyword, line:',line)
    while True:
        print('Quit with Control C')
if 'START' not in readst:
    print('Error, you need to start the program with the START keyword, line:',line)
    while True:
        print('Quit with Control C')

line = 0
while True:
    readline = read[line]
    def passing():
        if readline[:4] == 'pass':
            global line
            line += 1
    passing()

    def goto_def():
        if readline[:4] == 'goto':
            global line
            goto = readline.replace('goto','')
            goto = goto.replace('\n','')
            goto = goto.replace(' ','')
            number = goto.isdigit()
            if number == True:
                if len(read) >= line:
                    goto = int(goto)
                    line = goto -2
                else:
                    gotoerr()
            else:
                goto2 = stamplist.index(goto)
                stampgoto = stamplist[goto2 + 1]
                line = stampgoto         
    goto_def()

    def sleep_s():
        if readline[:1] == 's':
            readline_sleep = readline.replace('s','')
            readline_sleep = readline_sleep.replace('\n','')
            readline_sleep = readline_sleep.replace(' ', '')
            time.sleep(float(readline_sleep))
    sleep_s()

    def printf():
        if readline[:1] == ".":
            readpoint = readline.replace('.', '')
            readpoint = readpoint.replace('\n', '')
            print(readpoint)
    printf()

    def incpp():
        if readline[:2] == "++":
            readline_inc = readline.replace('++','')
            readline_inc = readline_inc.replace('\n','')
            readline_inc = readline_inc.replace(' ','')
            #print(readline_inc)
            pp = allvarlist.index(readline_inc)
            pp = pp + 1
            number = int(allvarlist[pp])
            number += 1
            allvarlist[pp] = number
            allvarlist[pp] = str(allvarlist[pp])
    incpp()

    def printf_no_newline():
        if readline[:1] == ",":
            read_virg = readline.replace(',','')
            read_virg = read_virg.replace('\n', '')
            print(read_virg, end= '')
    printf_no_newline()

    def operation():
        if readline[:2] == 'op' and readline[2] == ' ':
            countprep = str(readline)
            countprep = countprep.replace('op', '')
            countprep = countprep.replace(' ', '')
            countprep = countprep.replace('\n', '')

            if '+' in countprep:
                add = countprep.replace(' ', '')
                add = add.split('+')
                add = map(int,add)
                add = list(add)
                x = add[0]
                y = add[1]
                print(eval('x + y'))
            if '-' in countprep:
                sub = countprep.replace(' ', '')
                sub = sub.split('-')
                sub = map(int,sub)
                sub = list(sub)
                x = sub[0]
                y = sub[1]
                print(eval('x - y'))
            if 'x' in countprep:
                mul = countprep.replace(' ', '')
                mul = mul.split('x')
                mul = map(int,mul)
                mul = list(mul)
                x = mul[0]
                y = mul[1]
                print(eval('x * y'))
            if '/' in countprep:
                div = countprep.replace(' ', '')
                div = div.split('/')
                div = map(int,div)
                div = list(div)
                x = div[0]
                y = div[1]
                if y == 0 or x == 0:
                    print('you cannot divide by 0','line:',line)
                    #break
                print(eval('x / y'))
            
            if '^' in countprep:
                div = countprep.replace(' ', '')
                div = div.split('^')
                div = map(int,div)
                div = list(div)
                x = div[0]
                y = div[1]
                print(eval('x ** y'))
    operation()
    
    #not possible to transform in a function
    if readline[:1] == '<':
        readvar = readline.replace('\n','')
        readvar = readvar.replace('<','')
        readvar = readvar.split('=')
        for i in range(1):
            allvarlist.append(readvar)
            allvarlist = str(allvarlist)
            allvarlist = allvarlist.replace(' ','')
            allvarlist = allvarlist.split(',')
            allvarlist = str(allvarlist)
            allvarlist = allvarlist.replace('[','')
            allvarlist = allvarlist.replace(']','')
            allvarlist = allvarlist.replace('"','')
            allvarlist = allvarlist.replace("'",'')
            allvarlist = allvarlist.replace(' ','')
            allvarlist = allvarlist.split(',')
    
    def mem():
        if readline[:3] == 'mem':
            print(allvarlist)
    mem()

    #Garbage Collector
    def gb_collect():
        if readline[:1] == 'c':
            memlist = allvarlist
            number = 0
            dup = [x for i, x in enumerate(memlist) if i != memlist.index(x)] #iterate every duplicate item in the list
            dup = str(dup)
            dup = dup.replace('[','')
            dup = dup.replace(']','')
            dup = dup.replace("'",'')
            dup = dup.replace(" ",'')
            dup = dup.split(',')
            while number < len(dup):
                dup2 = dup[number]
                dup2digit = dup2.isdigit() #sort the list to find the letters
                if dup2digit == False: #continue if it is a letter
                    if dup2 == '': #if duplicated is empty break the collector loop
                        break
                    dup2int = memlist.index(dup2)
                    memlist.pop(dup2int) #pop the alone duplicated letter
                    dup3 = memlist.index(dup2)
                    dup3_digitcheck = dup2.isdigit()
                    if dup3_digitcheck == True: 
                        dup3 += 1
                        memlist.pop(dup3) #pop the number after the alone letter
                    number1is = str(memlist[0])
                    number2is = number1is.isdigit()
                    
                    if number2is == True: #if the first number of the list is a number pop it
                        memlist.pop(0) 
                    
                else:
                    dup2int = memlist.index(dup2)
                    checkdup = dup2int - 1
                    dupcheck = memlist[checkdup].isdigit()
                    if dupcheck == True:
                        memlist.pop(dup2int)
            
                    
                number += 1
                
            allvarlist = memlist 
    gb_collect()

    def delete_var():
        if readline[:3] == 'del':
            readdel = readline.replace('del', '')
            readdel = readdel.replace(' ', '')
            readdel = readdel.replace('\n', '')
            place = allvarlist.index(readdel)
            del allvarlist[place]
            del allvarlist[place]
    delete_var()

    def copy_var():
        if readline[:2] == 'cp':
            read_copy = readline.replace('cp', '')
            read_copy = read_copy.replace(' ', '')
            read_copy = read_copy.replace('\n', '')
            read_copy = read_copy.split(",")

            copy_from = read_copy[0]
            copy_to = read_copy[1]

            copy_from = allvarlist.index(copy_from)
            copy_to = allvarlist.index(copy_to)

            copy_from_value = copy_from + 1
            copy_to_value = copy_to + 1
            
            if len(allvarlist) <= copy_to_value:
                print('Error, you did not declare a variable!, line:',line)
            else:
                allvarlist[copy_to_value] = allvarlist[copy_from_value]
    copy_var()
        
       

    def input_var():
        if readline[:1] == '$':
            input_var = readline.replace('\n','')
            input_var = input_var.split('$')
            input_var = str(input_var)
            input_var = input_var.replace('[','')
            input_var = input_var.replace(']','')
            input_var = input_var.replace(',','')
            input_var = input_var.replace("'",'')
            input_var = input_var.replace(" ",'')
            var = allvarlist.index(input_var)
            newvar = var + 1
            allvarlist[newvar] = input()
            #input_check += 1
    input_var()

    def var_operation():
        if readline[:2] == 'ov':
            countprep = str(readline)
            countprep = countprep.replace('ov', '')
            countprep = countprep.replace(' ', '')
            countprep = countprep.replace('\n', '')
            if '+' in countprep:
                add = countprep.replace(' ', '')
                add = add.split('+')
                reset = str(add)
                reset = reset.replace('[', '')
                reset = reset.replace(']', '')
                reset = reset.replace("'", '')
                reset = reset.replace(" ", '')
                reset = reset.replace(",", '')
                out = reset.split('>>')
                out = out[1]
                var = allvarlist.index(out)
                var = var + 1
                add = reset
                if add[0] in allvarlist:
                    x = allvarlist.index(add[0])
                    x = x + 1
                    x = allvarlist[x]
                    if add[1] in allvarlist:
                        y = allvarlist.index(add[1])
                        y = y + 1
                        y = allvarlist[y]
                        x = int(x)
                        y = int(y)
                        result = eval('x + y')
                        result = str(result)
                        allvarlist[var] = result
                        
            if '-' in countprep:
                sub = countprep.replace(' ', '')
                sub = sub.split('-')
                reset = str(sub)
                reset = reset.replace('[', '')
                reset = reset.replace(']', '')
                reset = reset.replace("'", '')
                reset = reset.replace(" ", '')
                reset = reset.replace(",", '')
                out = reset.split('>>')
                out = out[1]
                var = allvarlist.index(out)
                var = var + 1
                #variable = allvarlist.append(out)
                sub = reset
                if sub[0] in allvarlist:
                    x = allvarlist.index(sub[0])
                    x = x + 1
                    x = allvarlist[x]
                    if sub[1] in allvarlist:
                        y = allvarlist.index(sub[1])
                        y = y + 1
                        y = allvarlist[y]
                        x = int(x)
                        y = int(y)
                        result = eval('x - y')
                        result = str(result)
                        allvarlist[var] = result
            if countprep[1] == 'x':
                mul = countprep.replace(' ', '')
                mul = mul.split('x')
                reset = str(mul)
                reset = reset.replace('[', '')
                reset = reset.replace(']', '')
                reset = reset.replace("'", '')
                reset = reset.replace(" ", '')
                reset = reset.replace(",", '')
                out = reset.split('>>')
                out = out[1]
                var = allvarlist.index(out)
                var = var + 1
                mul = reset
                if mul[0] in allvarlist:
                    x = allvarlist.index(mul[0])
                    x = x + 1
                    x = allvarlist[x]
                    if mul[1] in allvarlist:
                        y = allvarlist.index(mul[1])
                        y = y + 1
                        y = allvarlist[y]
                        x = int(x)
                        y = int(y)
                        result = eval('x * y')
                        result = str(result)
                        allvarlist[var] = result

            if '/' in countprep:
                div = countprep.replace(' ', '')
                div = div.split('/')
                reset = str(div)
                reset = reset.replace('[', '')
                reset = reset.replace(']', '')
                reset = reset.replace("'", '')
                reset = reset.replace(" ", '')
                reset = reset.replace(",", '')
                out = reset.split('>>')
                out = out[1]
                var = allvarlist.index(out)
                var = var + 1
                div = reset
                if div[0] in allvarlist:
                    x = allvarlist.index(div[0])
                    x = x + 1
                    x = allvarlist[x]
                    if div[1] in allvarlist:
                        y = allvarlist.index(div[1])
                        y = y + 1
                        y = allvarlist[y]
                        x = int(x)
                        y = int(y)
                        if y == 0 or x == 0:
                            print('you cannot divide by 0','line:',line)
                            #break
                        result = eval('x / y')
                        result = str(result)
                        allvarlist[var] = result
            if '^' in countprep:
                pwr = countprep.replace(' ', '')
                pwr = pwr.split('^')
                reset = str(pwr)
                reset = reset.replace('[', '')
                reset = reset.replace(']', '')
                reset = reset.replace("'", '')
                reset = reset.replace(" ", '')
                reset = reset.replace(",", '')
                out = reset.split('>>')
                out = out[1]
                var = allvarlist.index(out)
                var = var + 1
                pwr = reset
                if pwr[0] in allvarlist:
                    x = allvarlist.index(pwr[0])
                    x = x + 1
                    x = allvarlist[x]
                    if pwr[1] in allvarlist:
                        y = allvarlist.index(pwr[1])
                        y = y + 1
                        y = allvarlist[y]
                        x = int(x)
                        y = int(y)
                        result = eval('x ** y')
                        result = str(result)
                        allvarlist[var] = result
    var_operation()

    def roast():
        if readline[:5] == 'roast':
            print('C is gay')
            print('C++ too unnecessary')
            print('Rust is too dificult')
            print('Python is too mainstream')
            print('Functional programming sucks')
            print('OOP sucks dick')
            print('MaltaLang is king')
    roast()

   

    if readline[:3] == 'END':
        break
        f.close()
    if readline[:3] == 'START':
        pass

    def decrement():
        if readline[:2] == '--':
            readline_dec = readline.replace('--','')
            readline_dec = readline_dec.replace('\n','')
            pp = allvarlist.index(readline_dec)
            pp = pp + 1
            number = int(allvarlist[pp])
            number -= 1
            allvarlist[pp] = number
            allvarlist[pp] = str(allvarlist[pp])
    decrement()
    def var_no_newline():
        if readline[:1] == '>' and readline[1] != '>':
            readline_var = readline.replace('\n','')
            readline_var = readline_var.replace(' ','')
            readline_var = readline_var.split('>')
            varprint = allvarlist.index(readline_var[1])
            varprint = varprint + 1
            print(allvarlist[varprint], end = '')
    var_no_newline()

    def var_write():
        if readline[:2] == '>>':
            readline_var = readline.replace('\n','')
            readline_var = readline_var.replace(' ','')
            readline_var = readline_var.split('>')
            varprint_var = allvarlist.index(readline_var[2])
            varprint_var = varprint_var + 1
            print(allvarlist[varprint_var])
    var_write()
    
    #line += 1
    def conditions():
        if readline[:2] == 'if':
            global line
            readline_if = readline.replace('\n','')
            readline_if = readline_if.replace(' ','')
            readline_if = readline_if.replace('if','')
            readline_if = readline_if.replace('goto','')
            readline_if = readline_if.replace('else','')

            readline_if = readline_if.split(':')
            readline_if = str(readline_if)
            readline_if = readline_if.replace('[','')
            readline_if = readline_if.replace(']','')
            readline_if = readline_if.replace("'",'')
            readline_if = readline_if.replace('"','')
            readline_if = readline_if.replace(' ','')
            readline_if = readline_if.split(',')
            readline_cmpr = str(readline_if[0])

            if '<' in readline_if[0]:

                readline_cmpr = readline_cmpr.split('<')


                first_cmpr_arg = allvarlist.index(readline_cmpr[0])
                second_cmpr_arg = allvarlist.index(readline_cmpr[1])

                first_cmpr_arg += 1
                second_cmpr_arg += 1

                first_cmpr_arg = allvarlist[first_cmpr_arg]
                second_cmpr_arg = allvarlist[second_cmpr_arg]

                first_cmpr_digit = first_cmpr_arg.isdigit()
                second_cmpr_digit = second_cmpr_arg.isdigit()

                if first_cmpr_digit == True and second_cmpr_digit == True:
                    if int(first_cmpr_arg) < int(second_cmpr_arg):
                        goto = str(readline_if[1])
                        number = goto.isdigit()
                        goto2 = stamplist.index(goto)
                        stampgoto = stamplist[goto2 + 1]
                        line = stampgoto
                        #print(line)
                    else:
                        end_statement = stamplist.index(readline_if[2])
                        end_statement = stamplist[end_statement + 1]
                        line = end_statement
                else:

                    if first_cmpr_arg < second_cmpr_arg:
                        goto = str(readline_if[1])
                        number = goto.isdigit()
                        goto2 = stamplist.index(goto)
                        stampgoto = stamplist[goto2 + 1]
                        line = stampgoto
                    else:
                        end_statement = stamplist.index(readline[2])
                        end_statement = stamplist[end_statement + 1]
                        line = end_statement

            if '=' in readline[0]:
                
                readline_cmpr = readline_cmpr.split('=')


                first_cmpr_arg = allvarlist.index(readline_cmpr[0])
                second_cmpr_arg = allvarlist.index(readline_cmpr[1])

                first_cmpr_arg += 1
                second_cmpr_arg += 1

                first_cmpr_arg = allvarlist[first_cmpr_arg]
                second_cmpr_arg = allvarlist[second_cmpr_arg]

                first_cmpr_digit = first_cmpr_arg.isdigit()
                second_cmpr_digit = second_cmpr_arg.isdigit()

                if first_cmpr_digit == True and second_cmpr_digit == True:
                    if int(first_cmpr_arg) == int(second_cmpr_arg):
                        goto = str(readline[1])
                        number = goto.isdigit()
                        goto2 = stamplist.index(goto)
                        stampgoto = stamplist[goto2 + 1]
                        line = stampgoto
                    else:
                        end_statement = stamplist.index(readline[2])
                        end_statement = stamplist[end_statement + 1]
                        line = end_statement
                else:

                    if first_cmpr_arg == second_cmpr_arg:
                        goto = str(readline[1])
                        number = goto.isdigit()
                        goto2 = stamplist.index(goto)
                        stampgoto = stamplist[goto2 + 1]
                        line = stampgoto
                    else:
                        end_statement = stamplist.index(readline[2])
                        end_statement = stamplist[end_statement + 1]
                        line = end_statement

            if '>' in readline[0]:
                
                readline_cmpr = readline_cmpr.split('>')


                first_cmpr_arg = allvarlist.index(readline_cmpr[0])
                second_cmpr_arg = allvarlist.index(readline_cmpr[1])

                first_cmpr_arg += 1
                second_cmpr_arg += 1

                first_cmpr_arg = allvarlist[first_cmpr_arg]
                second_cmpr_arg = allvarlist[second_cmpr_arg]

                first_cmpr_digit = first_cmpr_arg.isdigit()
                second_cmpr_digit = second_cmpr_arg.isdigit()

                if first_cmpr_digit == True and second_cmpr_digit == True:
                    if int(first_cmpr_arg) > int(second_cmpr_arg):
                        goto = str(readline[1])
                        number = goto.isdigit()
                        goto2 = stamplist.index(goto)
                        stampgoto = stamplist[goto2 + 1]
                        line = stampgoto
                    else:
                        end_statement = stamplist.index(readline[2])
                        end_statement = stamplist[end_statement + 1]
                        line = end_statement
                else:

                    if first_cmpr_arg > second_cmpr_arg:
                        goto = str(readline[1])
                        number = goto.isdigit()
                        goto2 = stamplist.index(goto)
                        stampgoto = stamplist[goto2 + 1]
                        line = stampgoto
                    else:
                        end_statement = stamplist.index(readline[2])
                        end_statement = stamplist[end_statement + 1]
                        line = end_statement
    conditions()

    def while_loop():
        global line
        global readline
        global number
        if readline[:5] == 'while': #note make a check if is digit
            readline_while = readline.replace('\n','')
            readline_while = readline_while.replace('while','')
            readline_while = readline_while.split(':')
            readline_while = str(readline_while)
            readline_while = readline_while.replace(' ','')
            readline_while = readline_while.replace('[','')
            readline_while = readline_while.replace(']','')
            readline_while = readline_while.replace("'",'')
            readline_while = readline_while.replace('"','')
            readline_while = readline_while.replace('goto','')
            readline_while = readline_while.replace('else','')
            whilelist.append(readline_while)
            
            lenght = len(whilelist)
            if number < lenght:
                if whilelist != []:
                    while_readline = whilelist[number]
                    while_readline = while_readline.split(',')
                    args = str(while_readline[0])
                    if '=' in while_readline[0]:
                        args = args.split('=')
                            
                        while_first_arg = args[0]
                        while_second_arg = args[1]

                        while_first_arg = allvarlist.index(while_first_arg) + 1
                        while_second_arg = allvarlist.index(while_second_arg) + 1
                            
                        while_first_arg = allvarlist[while_first_arg]
                        while_second_arg = allvarlist[while_second_arg]
                        
                        while_first_arg_digit = while_first_arg.isdigit()
                        while_second_arg_digit = while_second_arg.isdigit()

                        if while_first_arg_digit == True and  while_second_arg_digit == True:
                            while int(while_first_arg) == int(while_second_arg):
                                while_first_arg = args[0]
                                while_second_arg = args[1]

                                while_first_arg = allvarlist.index(while_first_arg) + 1
                                while_second_arg = allvarlist.index(while_second_arg) + 1
                                    
                                while_first_arg = allvarlist[while_first_arg]
                                while_second_arg = allvarlist[while_second_arg]
                            
                                goto = str(while_readline[1])
                                number = goto.isdigit()
                                goto2 = stamplist.index(goto)
                                stampgoto = stamplist[goto2 + 1]

                                readline = read[line]

                                sleep_s()
                                printf()
                                incpp()
                                printf_no_newline()
                                operation()
                                mem()
                                gb_collect()
                                delete_var()
                                copy_var()
                                input_var()
                                var_operation()
                                roast()
                                decrement()
                                var_no_newline()
                                var_write()
                                conditions()
                                goto_def()
                                passing()
                                while_loop()
                                read_file_line()
                                end_statement = stamplist.index(str(while_readline[2]))
                                end_statement = stamplist[end_statement + 1] 
                                if line == end_statement - 1:
                                    line = stampgoto
                                line += 1
                            else:
                                end_statement = stamplist.index(str(while_readline[2]))
                                end_statement = stamplist[end_statement + 1] 
                                line = end_statement
                        else:
                            while while_first_arg == while_second_arg:
                                while_first_arg = args[0]
                                while_second_arg = args[1]

                                while_first_arg = allvarlist.index(while_first_arg) + 1
                                while_second_arg = allvarlist.index(while_second_arg) + 1
                                    
                                while_first_arg = allvarlist[while_first_arg]
                                while_second_arg = allvarlist[while_second_arg]
                            
                                goto = str(while_readline[1])
                                number = goto.isdigit()
                                goto2 = stamplist.index(goto)
                                stampgoto = stamplist[goto2 + 1]

                                readline = read[line]

                                sleep_s()
                                printf()
                                incpp()
                                printf_no_newline()
                                operation()
                                mem()
                                gb_collect()
                                delete_var()
                                copy_var()
                                input_var()
                                var_operation()
                                roast()
                                decrement()
                                var_no_newline()
                                var_write()
                                conditions()
                                goto_def()
                                passing()
                                while_loop()
                                read_file_line()
                                end_statement = stamplist.index(str(while_readline[2]))
                                end_statement = stamplist[end_statement + 1] 
                                if line == end_statement - 1:
                                    line = stampgoto
                                line += 1
                            else:
                                end_statement = stamplist.index(str(while_readline[2]))
                                end_statement = stamplist[end_statement + 1] 
                                line = end_statement
                    if '<' in while_readline[0]:
                        args = args.split('<')
                            
                        while_first_arg = args[0]
                        while_second_arg = args[1]

                        while_first_arg = allvarlist.index(while_first_arg) + 1
                        while_second_arg = allvarlist.index(while_second_arg) + 1
                            
                        while_first_arg = allvarlist[while_first_arg]
                        while_second_arg = allvarlist[while_second_arg]
                        while_first_arg_digit = while_first_arg.isdigit()
                        while_second_arg_digit = while_second_arg.isdigit()

                        if while_first_arg_digit == True and  while_second_arg_digit == True:
                            while int(while_first_arg) < int(while_second_arg):
                                while_first_arg = args[0]
                                while_second_arg = args[1]

                                while_first_arg = allvarlist.index(while_first_arg) + 1
                                while_second_arg = allvarlist.index(while_second_arg) + 1
                                    
                                while_first_arg = allvarlist[while_first_arg]
                                while_second_arg = allvarlist[while_second_arg]
                            
                                goto = str(while_readline[1])
                                number = goto.isdigit()
                                goto2 = stamplist.index(goto)
                                stampgoto = stamplist[goto2 + 1]

                                
                                readline = read[line]
                                

                                sleep_s()
                                printf()
                                incpp()
                                printf_no_newline()
                                operation()
                                mem()
                                gb_collect()
                                delete_var()
                                copy_var()
                                input_var()
                                var_operation()
                                roast()
                                decrement()
                                var_no_newline()
                                var_write()
                                conditions()
                                goto_def()
                                passing()
                                read_file_line()
                                
                                #while_loop()
                                end_statement = stamplist.index(str(while_readline[2]))
                                end_statement = stamplist[end_statement + 1] 
                                if line == end_statement - 1:
                                    line = stampgoto
                                line += 1
                            else:
                                end_statement = stamplist.index(str(while_readline[2]))
                                end_statement = stamplist[end_statement + 1] 
                                line = end_statement
                        else:
                            while while_first_arg < while_second_arg:
                                while_first_arg = args[0]
                                while_second_arg = args[1]

                                while_first_arg = allvarlist.index(while_first_arg) + 1
                                while_second_arg = allvarlist.index(while_second_arg) + 1
                                    
                                while_first_arg = allvarlist[while_first_arg]
                                while_second_arg = allvarlist[while_second_arg]
                            
                                goto = str(while_readline[1])
                                number = goto.isdigit()
                                goto2 = stamplist.index(goto)
                                stampgoto = stamplist[goto2 + 1]

                                readline = read[line]

                                sleep_s()
                                printf()
                                incpp()
                                printf_no_newline()
                                operation()
                                mem()
                                gb_collect()
                                delete_var()
                                copy_var()
                                input_var()
                                var_operation()
                                roast()
                                decrement()
                                var_no_newline()
                                var_write()
                                conditions()
                                goto_def()
                                passing()
                                read_file_line()
                                #while_loop()
                                end_statement = stamplist.index(str(while_readline[2]))
                                end_statement = stamplist[end_statement + 1] 
                                if line == end_statement - 1:
                                    line = stampgoto
                                line += 1
                            else:
                                end_statement = stamplist.index(str(while_readline[2]))
                                end_statement = stamplist[end_statement + 1] 
                                line = end_statement

                    if '>' in while_readline[0]:
                        args = args.split('>')
                            
                        while_first_arg = args[0]
                        while_second_arg = args[1]

                        while_first_arg = allvarlist.index(while_first_arg) + 1
                        while_second_arg = allvarlist.index(while_second_arg) + 1
                            
                        while_first_arg = allvarlist[while_first_arg]
                        while_second_arg = allvarlist[while_second_arg]
                        while_first_arg_digit = while_first_arg.isdigit()
                        while_second_arg_digit = while_second_arg.isdigit()

                        if while_first_arg_digit == True and  while_second_arg_digit == True:
                            while int(while_first_arg) > int(while_second_arg):
                                while_first_arg = args[0]
                                while_second_arg = args[1]

                                while_first_arg = allvarlist.index(while_first_arg) + 1
                                while_second_arg = allvarlist.index(while_second_arg) + 1
                                    
                                while_first_arg = allvarlist[while_first_arg]
                                while_second_arg = allvarlist[while_second_arg]
                            
                                goto = str(while_readline[1])
                                number = goto.isdigit()
                                goto2 = stamplist.index(goto)
                                stampgoto = stamplist[goto2 + 1]

                                readline = read[line]
                                sleep_s()
                                printf()
                                incpp()
                                printf_no_newline()
                                operation()
                                mem()
                                gb_collect()
                                delete_var()
                                copy_var()
                                input_var()
                                var_operation()
                                roast()
                                decrement()
                                var_no_newline()
                                var_write()
                                conditions()
                                goto_def()
                                passing()
                                read_file_line()
                                #while_loop()
                                end_statement = stamplist.index(str(while_readline[2]))
                                end_statement = stamplist[end_statement + 1] 
                                if line == end_statement - 1:
                                    line = stampgoto
                                line += 1
                            else:
                                end_statement = stamplist.index(str(while_readline[2]))
                                end_statement = stamplist[end_statement + 1] 
                                line = end_statement
                        else:
                            while while_first_arg > while_second_arg:
                                while_first_arg = args[0]
                                while_second_arg = args[1]

                                while_first_arg = allvarlist.index(while_first_arg) + 1
                                while_second_arg = allvarlist.index(while_second_arg) + 1
                                    
                                while_first_arg = allvarlist[while_first_arg]
                                while_second_arg = allvarlist[while_second_arg]
                            
                                goto = str(while_readline[1])
                                number = goto.isdigit()
                                goto2 = stamplist.index(goto)
                                stampgoto = stamplist[goto2 + 1]

                                readline = read[line]
                                sleep_s()
                                printf()
                                incpp()
                                printf_no_newline()
                                operation()
                                mem()
                                gb_collect()
                                delete_var()
                                copy_var()
                                input_var()
                                var_operation()
                                roast()
                                decrement()
                                var_no_newline()
                                var_write()
                                conditions()
                                goto_def()
                                passing()
                                while_loop()
                                read_file_line()
                                end_statement = stamplist.index(str(while_readline[2]))
                                end_statement = stamplist[end_statement + 1] 
                                if line == end_statement - 1:
                                    line = stampgoto
                                line += 1
                            else:
                                end_statement = stamplist.index(str(while_readline[2]))
                                end_statement = stamplist[end_statement + 1] 
                                line = end_statement



                    number += 1
    while_loop()

    def open_file():
        global allfilelist
        global var
        #[file = open teste.txt, r
        if readline[:1] == '[':
            open_readline = readline.replace('\n','')
            open_readline = open_readline.replace('open','')
            open_readline = open_readline.replace('[','')
            open_readline = open_readline.replace(' ','')
            open_readline = open_readline.split(',')
            open_readline_partone = open_readline[0].split('=')
            open_readline_parttwo = open_readline[1]
            
            allfilelist.append(open_readline_partone[0])
            file_argv = open_readline_partone[1]
            var = allfilelist.index(open_readline_partone[0])
            var = allfilelist[var]

            var = open(file_argv,open_readline_parttwo)

    open_file()

    def read_file_line(): #readline, a
        global var
        global allvarlist

        if readline[:8] == 'readline':
            read_file_line = readline.replace('readline','')
            read_file_line = read_file_line.replace('\n','')
            read_file_line = read_file_line.replace(' ','')
            read_file_line = read_file_line.replace(',','')
            line_var = allvarlist.index(read_file_line) + 1
            line_var = allvarlist[line_var]
            read_list.append(var.readlines())
            read = read_list[0]

            len_read_list.append(len(read))
            len_read = len_read_list[0]
            line_var = int(line_var)
            
            if line_var <= int(len_read):
                read_specific_line = read[line_var]
                read_specific_line = read_specific_line.replace('\n','')
                print(read_specific_line)
    read_file_line()


    def close_file(): #]file.close
        global var
        if readline[:1] == ']':
            var.close()
    close_file()

    def read_file():
        global var
        if readline[:8] == 'readfile':
            print(var.read())
    read_file()

    def write_file():
        global allvarlist
        global var
        if readline[:5] == 'write':
            write_file_read = readline.replace('\n','')
            write_file_read = write_file_read.replace(' ','')
            write_file_read = write_file_read.replace('write','')
            write_file_read = write_file_read.replace(',','')

            what_write = allvarlist.index(write_file_read) + 1
            what_write = allvarlist[what_write]
            print(what_write)
            if what_write == '*nl':
                var.write('\n')
            else:
                var.write(what_write)
            #print(what_write)
    write_file()

    line += 1    
#end_time = datetime.now()
#print(end_time - start_time)