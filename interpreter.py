if not __name__ == "__main__":
    exit("ERROR: The MAL interpreter should not be run as a library!")
from enum import Enum
f = open('code.mlt', 'r')

while f:

    stringcheck = f.readline(100000)
    checkpoint= stringcheck[:1]
    checkend= stringcheck[:3]
    checkop = stringcheck[:2]
    checknum = stringcheck[:9999999999999999999999]

    if checkpoint == ".":
        replacepoint = stringcheck.replace('.', '')
        replacespace = replacepoint.replace('\n', '')
        print (replacespace)

    if checkend == 'END':
            f.close()
            break
    if checkop == "op":
        replaceop = stringcheck.replace('op', '')
        replaceop2 = replaceop.replace(' ', '')
        replaceop3 = replaceop2.replace('\n', '')
        operation = list(replaceop3)

        if '+' in operation:
            replaceop4 = replaceop3.replace(' ', '')
            number = replaceop4.split('+')
            newnumber = map(int,number)
            newnumberlist = list(newnumber)
            x = newnumberlist[0]
            y = newnumberlist[1]
            print(eval('x + y'))

        if '-' in operation:
            replaceop4 = replaceop3.replace(' ', '')
            number = replaceop4.split('-')
            newnumber = map(int,number)
            newnumberlist = list(newnumber)
            x = newnumberlist[0]
            y = newnumberlist[1]
            print(eval('x - y'))

        if '/' in operation:
            replaceop4 = replaceop3.replace(' ', '')
            number = replaceop4.split('/')
            newnumber = map(int,number)
            newnumberlist = list(newnumber)
            x = newnumberlist[0]
            y = newnumberlist[1]
            print(eval('x / y'))

        if 'x' in operation:
            replaceop4 = replaceop3.replace(' ', '')
            number = replaceop4.split('x')
            newnumber = map(int,number)
            newnumberlist = list(newnumber)
            x = newnumberlist[0]
            y = newnumberlist[1]
            print(eval('x * y'))
