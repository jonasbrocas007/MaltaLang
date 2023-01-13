def collect(allvarlist, all_valuelist):
    #print(allvarlist)
    #print(all_valuelist)

    memlist = allvarlist
    valuelist = all_valuelist
    number = 0
    dup = [x for i, x in enumerate(memlist) if i != memlist.index(x)]  # iterate every duplicate item in the list # noqa
    dup = str(dup)
    dup = dup.replace('[', '')
    dup = dup.replace(']', '')
    dup = dup.replace("'", '')
    dup = dup.replace(" ", '')
    dup = dup.split(',')
    while number < len(dup):
        dup2 = dup[number]
        dup2digit = dup2.isdigit()  # sort the list to find the letters
        if dup2digit is False:  # continue if it is a letter
            if dup2 == '':  # if duplicated is empty break the loop
                break
            dup2int = memlist.index(dup2)
            memlist.pop(dup2int)
            valuelist.pop(dup2int)  # pop the alone duplicated letter
            dup3 = memlist.index(dup2)
            dup3_digitcheck = dup2.isdigit()

            if dup3_digitcheck is True:
                dup3 += 1
                memlist.pop(dup3)
                valuelist.pop(dup3)
                all  # pop number after the alone char
                number1is = str(memlist[0])
                number2is = number1is.isdigit()

                if number2is is True:  # if the first item is a number pop
                    memlist.pop(0)
                    valuelist.pop(0)

            else:
                dup2int = memlist.index(dup2)
                checkdup = dup2int - 1
                dupcheck = memlist[checkdup].isdigit()
                if dupcheck is True:
                    memlist.pop(dup2int)
                    all_valuelist.pop(dup2int)

            number += 1

        collect.allvarlist = memlist
        collect.all_valuelist = valuelist
        return allvarlist
        return all_valuelist