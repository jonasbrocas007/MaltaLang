def println(string, varlist, var_valuelist):
    if string[:1] == " ":
        string = string[1:]

    string = string.replace("%n", "\n")

    if '"' in string:
        string = string.replace('"',"")
    else:
        variable_name = varlist.index(string)
        string = var_valuelist[variable_name]
    print(string)      

def printf(string, varlist, var_valuelist):
    string = string.replace(" ","")
    string = string.replace("_", " ")
    string = string.replace("%n", "\n")
    if '"' in string:
        string = string.replace('"',"")
    else:
        variable_name = varlist.index(string)
        string = var_valuelist[variable_name]
    print(string, end = "")