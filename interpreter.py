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
            replaceop = replaceop.replace(' ', '')
            number = replaceop.split('+')
            replaceop = map(int,replaceop)
            replaceop = list(replaceop)
            x = replaceop[0]
            y = replaceop[1]
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
        replace = stringcheck.replace('.', '')
        replace = replace.replace('\n', '')
        print (replace)

    if checkend == 'END':
            f.close()
            break
    if checkend == '':
        pass
    if checkop == "op":
        basic_enum()

    if checkpoint == '<':
        #this was not working at all, need to rewrite
        
#if algo = 1, then .mekie
    if checkop == 'if':
        iffn = stringcheck.replace('if', '')
        iffn = iffn.replace('\n', '')
        iffn = iffn.split('=')
        iffn = str(iffn)
        iffn = iffn.replace("'",'')
        iffn = iffn.replace('[','')
        iffn = iffn.replace(']','')
        iffn = iffn.replace(' ','')
        iffn = iffn.split(',')
        iffn = iffn.replace(' ','')
        iffn = str(iffn)

        iffn = iffn.split('.')
        iffn = str(iffn)
        iffn = iffn.replace("'",'')
        iffn = iffn.replace('[','')
        iffn = iffn.replace(']','')
        iffn = iffn.replace(',','')
        iffn = iffn.replace('"','')
        iffn = iffn.split()

        
        if newlist[2] == 'then' or newlist[2] == 't':
            if newlist[3]:
                print(newlist[3])
        if newlist[2] == 'thenop' or newlist[2] == 'top':
            if '+' in newlist[3]:
                
            if '-' in newlist[3]:
               
            if '/' in newlist[3]:
                    
            if 'x' in newlist[3]:
                    
    if checkpoint == '>':
        #need to rewrite

                    
        
