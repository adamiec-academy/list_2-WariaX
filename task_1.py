def remove_parentheses(text):
    result = ""
    is_inside = False

    for x in text:
        if x == "(":            
            is_inside = True

        elif x == ")":            
            is_inside = False

        elif is_inside == False:
            result += x            

    return result.replace ("  "," ")
