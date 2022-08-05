if not __name__ == "__main__":
    exit("ERROR: The MAL interpreter should not be run as a library!")
from enum import Enum
f = open('code.mlt', 'r')

def basic_enum():
        replaceop = stringcheck.replace('op', '')
        replaceop = replaceop.replace(' ', '')
        replaceop = replaceop.replace('\n', '')
        operation = list(replaceop)
        if '+' in operation:
            replaceop4
 = replaceop3.replace(' ', '')
            number = replaceop4.split('+')
            newnumber = map(int,number)
            newnumberlist = list(newnumber)
            x = newnumberlist[0]
            y = newnumberlist[1]
            print(eval('x + y'))

        if '-' in operation:
            replaceop = replaceop.replace(' ', '')
            replaceop = replaceop.split('-')
            replaceop = map(int,replaceop)
            replaceop = list(replaceop)
            x = replaceop[0]
            y = replaceop[1]
            print(eval('x - y'))

        if '/' in operation:
            replaceop = replaceop.replace(' ', '')
            replaceop = replaceop.split('/')
            replaceop = map(int,replaceop)
            replaceop = list(replaceop)
            x = replaceop[0]
            y = replaceop[1]
            print(eval('x / y'))

        if 'x' in operation:
            replaceop = replaceop.replace(' ', '')
            replaceop  = replaceop.split('x')
            replaceop = map(int,replaceop)
            replaceop = list(replaceop)
            x = replaceop[0]
            y = replaceop[1]
            print(eval('x * y'))
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
    if checkend == '':
        pass
    if checkop == "op":
        basic_enum()

    if checkpoint == '<':
        fn = stringcheck.replace('<','')
        fn2 = fn.replace('\n','')
        func = fn2.split('=')
        newfn = map(str,func)
        newfunc = list(newfn)
        var = newfunc[0]
        val = newfunc[1]
        operationval = list(val)
        
#if algo = 1, then .mekie
    if checkop == 'if':
        replaceif = stringcheck.replace('if', '')
        replaceif2 = replaceif.replace('\n', '')
        splitlist = replaceif2.split('=')
        splitmekie = str(splitlist)
        mekiereplace = splitmekie.replace("'",'')
        mekiereplace2 = mekiereplace.replace('[','')
        mekiereplace3 = mekiereplace2.replace(']','')
        mekiereplace4 = mekiereplace3.replace(' ','')
        splitthen = mekiereplace4.split(',')
        val2 = val.replace(' ','')
        newsplitstring = str(splitthen)

        splitthen2 = newsplitstring.split('.')
        splitthen3 = str(splitthen2)
        replace0 = splitthen3.replace("'",'')
        mekiere1 = replace0.replace('[','')
        mekiere2 = mekiere1.replace(']','')
        mekiere3 = mekiere2.replace(',','')
        mekiere4 = mekiere3.replace('"','')
        newlist = mekiere4.split()

        if newlist[1] == val2:
            if newlist[2] == 'then' or newlist[2] == 't':
                if newlist[3]:
                    print(newlist[3])
            if newlist[2] == 'thenop' or newlist[2] == 'top':
                if '+' in newlist[3]:
                    replacetop4 = newlist[3].replace(' ', '')
                    numbertop = replacetop4.split('+')
                    newnumbertop = map(int,numbertop)
                    newnumberlisttop = list(newnumbertop)
                    x = newnumberlisttop[0]
                    y = newnumberlisttop[1]
                    val = print(eval('x + y'))
                if '-' in newlist[3]:
                    replacetop4 = newlist[3].replace(' ', '')
                    numbertop = replacetop4.split('-')
                    newnumbertop = map(int,numbertop)
                    newnumberlisttop = list(newnumbertop)
                    x = newnumberlisttop[0]
                    y = newnumberlisttop[1]
                    val = print(eval('x - y'))
                if '/' in newlist[3]:
                    replacetop4 = newlist[3].replace(' ', '')
                    numbertop = replacetop4.split('/')
                    newnumbertop = map(int,numbertop)
                    newnumberlisttop = list(newnumbertop)
                    x = newnumberlisttop[0]
                    y = newnumberlisttop[1]
                    val = print(eval('x / y'))
                if 'x' in newlist[3]:
                    replacetop4 = newlist[3].replace(' ', '')
                    numbertop = replacetop4.split('x')
                    newnumbertop = map(int,numbertop)
                    newnumberlisttop = list(newnumbertop)
                    x = newnumberlisttop[0]
                    y = newnumberlisttop[1]
                    val = print(eval('x x y'))
    if checkpoint == '>':
        if '+' in operationval:
            replaceop4 = val.replace(' ', '')
            number = replaceop4.split('+')
            newnumber = map(int,number)
            newnumberlist = list(newnumber)
            x = newnumberlist[0]
            y = newnumberlist[1]
            val = print(eval('x + y'))
        if '-' in operationval:
            replaceop4 = val.replace(' ', '')
            number = replaceop4.split('-')
            newnumber = map(int,number)
            newnumberlist = list(newnumber)
            x = newnumberlist[0]
            y = newnumberlist[1]
            val = print(eval('x - y'))

        if '/' in operationval:
            replaceop4 = val.replace(' ', '')
            number = replaceop4.split('/')
            newnumber = map(int,number)
            newnumberlist = list(newnumber)
            x = newnumberlist[0]
            y = newnumberlist[1]
            val = print(eval('x / y'))

        if 'x' in operationval:
            replaceop4 = val.replace(' ', '')
            number = replaceop4.split('x')
            newnumber = map(int,number)
            newnumberlist = list(newnumber)
            x = newnumberlist[0]
            y = newnumberlist[1]
            val = print(eval('x * y'))
        print(val)

                    
        
