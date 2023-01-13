def ifs(condition, allvarlist, all_valuelist, stamplist, stampline_list, line):
    ifs.line = 0
    ifs.true = True
    ifs.endline = 0
    variable_operating = 0
    condition = condition.split(":")
    condition_statement = condition[0]
    condition_statement = condition_statement.split(" ")

    if str(condition_statement[-1]) == "":
        condition_statement = condition_statement [:-1]

    while True:
        if condition_statement[0] == '':
            condition_statement.pop(0)

        if condition_statement[variable_operating] not in allvarlist:
            variable_operating += 1
        else:
            if condition_statement[0] in allvarlist:
                value_index = allvarlist.index(condition_statement[0])  #transform variable in the left side to its value
                condition_statement[0] = all_valuelist[value_index]

            if condition_statement[2] in allvarlist:
                value_index = allvarlist.index(condition_statement[2])  #transform variable in the right side to its value
                condition_statement[2] = all_valuelist[value_index]

            compar_one = condition_statement[0]
            compar_two = condition_statement[2]

            stamps = condition[1]
            stamps = stamps.replace(" ", "")
            stamps = stamps.split(",")
            endline = stamplist.index(stamps[1])
            ifs.endline = stampline_list[endline]

            if "=" in condition_statement:
                if str(compar_one) == str(compar_two):
                    ifs.true = True

                    start = stamps[0]
                    start = stamplist.index(start)
                    ifs.line = stampline_list[start]
                    return ifs.line
                else:
                    ifs.true = False
                    end = stamps[1]
                    end = stamplist.index(end)
                    ifs.line = stampline_list[end]
                    return ifs.line
            #ifs.true = False
            if "!=" in condition_statement:
                if str(compar_one) != str(compar_two):
                    ifs.true = True
                    start = stamps[0]
                    start = stamplist.index(start)
                    ifs.line = stampline_list[start]
                    return ifs.line
                else:
                    ifs.true = False
                    end = stamps[1]
                    end = stamplist.index(end)
                    ifs.line = stampline_list[end]
                    return ifs.line
            #ifs.true = False
            if "<" in condition_statement:
                if float(compar_one) < float(compar_two):
                    ifs.true = True
                    start = stamps[0]    
                    start = stamplist.index(start)
                    ifs.line = stampline_list[start]
                    return ifs.line
                else:
                    ifs.true = False
                    end = stamps[1]
                    end = stamplist.index(end)
                    ifs.line = stampline_list[end]
                    return ifs.line
            #ifs.true = False
            if "<=" in condition_statement: 
                if float(compar_one) <= float(compar_two):
                    ifs.true = True
                    start = stamps[0]    
                    start = stamplist.index(start)
                    ifs.line = stampline_list[start]
                    return ifs.line
                else:
                    ifs.true = False
                    end = stamps[1]
                    end = stamplist.index(end)
                    ifs.line = stampline_list[end]
                    return ifs.line
            #ifs.true = False
            if ">" in condition_statement:
                if float(compar_one) > float(compar_two):
                    ifs.true = True
                    start = stamps[0]    
                    start = stamplist.index(start)
                    ifs.line = stampline_list[start]
                    return ifs.line
                else:
                    ifs.true = False
                    end = stamps[1]
                    end = stamplist.index(end)
                    ifs.line = stampline_list[end]
                    return ifs.line
            #ifs.true = False
            if ">=" in condition_statement:
                if float(compar_one) >= float(compar_two):
                    ifs.true = True
                    start = stamps[0]    
                    start = stamplist.index(start)
                    ifs.line = stampline_list[start]
                    return ifs.line
                else:
                    ifs.true = False
                    end = stamps[1]
                    end = stamplist.index(end)
                    ifs.line = stampline_list[end]
                    return ifs.line
            #ifs.true = False
        if variable_operating < len(condition_statement) - 1:
            variable_operating += 1

        if variable_operating >= len(condition_statement):
            break