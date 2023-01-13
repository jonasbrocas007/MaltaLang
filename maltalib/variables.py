import maltalib.garbage_collector
def create_var(expression, varlist, var_valuelist):
    variable_type = expression[-1]
    expression = expression.replace("%n", "\n")

    if variable_type == "s":
        is_type = 0

    if variable_type == "i":
        is_type = 1   

    if variable_type == "f":
        is_type = 2

    expression = expression[:-1]   
    expression = expression.split("=")

    variable_name = expression[0]
    variable_name = variable_name.replace(" ", "")
    variable_value = expression[1]

    if variable_value[:1] == " ":
        variable_value = variable_value[1:] 

    varlist.append(variable_name)

    if variable_type == "s":
        var_valuelist.append(str(variable_value))

    if variable_type == "i":
        var_valuelist.append(int(variable_value))

    if variable_type == "f":
        var_valuelist.append(float(variable_value))

    maltalib.garbage_collector.collect(varlist, var_valuelist)
    
def input_var(variable, varlist, var_valuelist):
    variable = variable.replace(" ", "")
    is_type = 0

    if variable[-1] == 's':
        variable = variable[:-1]
        is_type = 0

    if variable[-1] == 'i':
        variable = variable[:-1]
        is_type = 1

    if variable[-1] == 'f':
        variable = variable[:-1]
        is_type = 2

    variable_index = varlist.index(variable) #find variable index to look at the value later

    if is_type == 0:
        var_valuelist[variable_index] = str(input())

    if is_type == 1:
        var_valuelist[variable_index] = int(input())

    if is_type == 2:
        var_valuelist[variable_index] = float(input())

    maltalib.garbage_collector.collect(varlist, var_valuelist)

def copy_var(expression, varlist, var_valuelist):
    expression = expression.replace(" ", "")
    expression = expression.split(",")

    copy_to = expression[0]
    copy_from = expression[1]

    copy_to_index = varlist.index(copy_to)
    copy_from_index = varlist.index(copy_from)

    var_valuelist[copy_to_index] = var_valuelist[copy_from_index]

    maltalib.garbage_collector.collect(varlist, var_valuelist)

def delete_var(expression, varlist, var_valuelist):
    variable = varlist.index(expression)
    varlist.pop(variable)
    var_valuelist.pop(variable)
    delete_var.varlist = varlist
    delete_var.var_valuelist = var_valuelist

    maltalib.garbage_collector.collect(varlist, var_valuelist)
    
def shift(expression, varlist, var_valuelist):
    expression = expression.replace(" ","")
    expression = expression.split("<-")

    if '+' in expression[1]:
        copy_from = expression[1].split("+")
        copy_from_index = varlist.index(copy_from[0])
        copy_from_index += int(copy_from[1])
        copy_from = varlist[copy_from_index]
    
    if '-' in expression[1]:
        copy_from = expression[1].split("-")
        copy_from_index = varlist.index(copy_from[0])
        copy_from_index -= int(copy_from[1])
        copy_from = varlist[copy_from_index]
    
    copy_to = expression[0]
    expression = copy_to+ ',' + copy_from
    copy_var(expression, varlist, var_valuelist)


    maltalib.garbage_collector.collect(varlist, var_valuelist)