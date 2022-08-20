if not __name__ == "__main__":
    exit("ERROR: The MAL interpreter should not be run as a library!")
from enum import Enum
f = open('code.mlt', 'r')
read_header = -1
read_op = -1
read_end = -1
read_var = -1
read_cout = -1
var_count = -1
if_count = -1
read_loop = -1
read_input = -1
#ifs
fread_header = -1
fread_op = -1
fread_end = -1
fread_var = -1
fread_cout = -1
fvar_count = -1

checker = '.'
op_checker = 'op'
end_checker = 'END'
var_checker = '<'
cout_checker = '>'
if_checker = 'if'
loop_checker = 'lp'
input_checker = ''
allvarlist = []
rows = []
read = f.readlines()
for checker in read:
    read_header += 1
    readline = read[read_header]
    if readline[0] == ".":
        readpoint = readline.replace('.', '')
        readpoint = readpoint.replace('\n', '')
        print(readpoint)
        if '>' in readline:
            print('debug,yes')

for op_checker in read:
    read_op += 1
    readline = read[read_op]
    if readline[:2] == 'op':
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
            print(eval('x / y'))
for var_checker in read:
    read_var += 1
    readline = read[read_var]
    if readline[:1] == '<':
        var_count += 1
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
            allvarlistf = allvarlist.split(',')

for cout_checker in read:
    read_cout += 1
    readline = read[read_cout]
    if readline[0] == '>':
        readline = readline.replace('\n','')
        readline = readline.split('>')
        varprint = allvarlist.index(readline[1])
        varprint = varprint + 1
        print(allvarlist[varprint])

for if_checker in read:
    if_count += 1
    readline = read[if_count]
    if readline[:2] == 'if':
        readif = readline.replace('\n','')
        readif = readif.replace('if','')
        readif = readif.replace('<','')
        readif = readif.replace(' ','')
        readif = readif.split(':')
        readvar = readif[0]
        readvar = readvar.split('=')
        readvarcheck = allvarlist.index(readvar[0])
        if readvar[readvarcheck] == allvarlistf[readvarcheck]:
            if readvar[readvarcheck + 1] == allvarlistf[readvarcheck + 1]:
                fread_op += 1
                readline = read[fread_op]
                if 'op' in readif[1]:
                    countprep = str(readif[1])
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
                        print(eval('x / y'))
                    if '.' in readif[1]:
                        print(readif[1])
for end_checker in read:
    read_end += 1
    readline = read[read_end]
    if readline[:3] == 'END':
        f.close()

for loop_checker in read:
    read_loop += 1
    readline = read[read_loop]
    if readline[:2] == 'lp':
        readlp = readline.replace('lp','')
        readlp = readlp.replace('\n','')
        readlp = readlp.replace(' ','')
        readlp = readlp.split('/')
        loopnumber = int(readlp[1])
        if '.' in readline:
            readlp = str(readlp[0])
            readlp = readlp.replace('.','')
            while loopnumber > 0:
                loopnumber -= 1
                print(readlp)
        if '>' in readline:
            readlp = str(readlp[0])
            readline = readline.replace('\n','')
            readline = readline.replace('lp','')
            readline = readline.replace('>','')
            readline = readline.replace(' ','')
            readline = readline.split('/')
            while loopnumber > 0:
                loopnumber -= 1
                varprint = allvarlistf.index(readline[0])
                varprint = varprint + 1
                print(allvarlistf[varprint])

    if readline[:3] == 'lpo':
        readlp = readline.replace('lpo','')
        readlp = readlp.replace('\n','')
        readlp = readlp.replace(' ','')
        readlp = readlp.split('/')
        loopnumber = int(readlp[1])
        if '+' in readline:
            while loopnumber > 0:
                loopnumber -= 1
                add = readlp[0]
                add = add.split('+')
                add = map(int,add)
                add = list(add)
                x = add[0]
                y = add[1]
                print(eval('x + y'))
        if '-' in readline:
            while loopnumber > 0:
                loopnumber -= 1
                add = readlp[0]
                add = add.split('-')
                add = map(int,add)
                add = list(add)
                x = add[0]
                y = add[1]
                print(eval('x - y'))
        if 'x' in readline:
            while loopnumber > 0:
                loopnumber -= 1
                add = readlp[0]
                add = add.split('x')
                add = map(int,add)
                add = list(add)
                x = add[0]
                y = add[1]
                print(eval('x * y'))
        if '/' in readline:
            while loopnumber > 0:
                loopnumber -= 1
                add = readlp[0]
                add = add.split('/')
                add = map(int,add)
                add = list(add)
                x = add[0]
                y = add[1]
                print(eval('x / y'))
