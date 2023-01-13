import maltalib.garbage_collector
def calculator(expression, varlist, all_valuelist):
    variable_operating = 0
    expression = expression.split(">>")
    operation = expression[0]
    operation = operation.split(" ")
    is_type = -1

    if str(operation[-1]) == "":
        operation = operation[:-1]

    while str(operation[variable_operating]).isdigit() == False:

        if operation[variable_operating] == '':
            variable_operating += 1

        if operation[variable_operating] not in varlist:
            if variable_operating < len(operation) - 1:
                variable_operating += 1
            else:
                break

        else:
            value_index = varlist.index(operation[variable_operating])
            operation[variable_operating] = all_valuelist[value_index]

            if variable_operating < len(operation) - 1:
                variable_operating += 1
    
    
    operation = str(operation)
    operation = operation.replace("[", "")
    operation = operation.replace("]", "")
    operation = operation.replace("'", "")
    operation = operation.replace(",", "")
    result = eval(operation)
        
    store_in = expression[1]
    store_in = store_in.replace(" ","")

    if str(store_in[-1]) == "s":
        is_type = 0
        store_in = store_in[:-1]

    if str(store_in[-1]) == "i":
        is_type = 1
        store_in = store_in[:-1]

    if str(store_in[-1]) == "f":
        is_type = 2
        store_in = store_in[:-1]

    store_in = varlist.index(store_in)

    if is_type == 0:
        all_valuelist[store_in] = str(result)

    if is_type == 1:
        all_valuelist[store_in] = int(result)

    if is_type == 2:
        all_valuelist[store_in] = float(result)

    maltalib.garbage_collector.collect(varlist, all_valuelist)
def increment(expression, varlist, all_valuelist):
    variable_index = varlist.index(expression)
    all_valuelist[variable_index] += 1
    increment.varlist = varlist
    increment.all_valuelist = all_valuelist

    maltalib.garbage_collector.collect(varlist, all_valuelist)

def decrement(expression, varlist, all_valuelist):
    variable_index = varlist.index(expression)
    all_valuelist[variable_index] -= 1

    maltalib.garbage_collector.collect(varlist, all_valuelist)