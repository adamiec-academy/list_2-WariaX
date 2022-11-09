def remove_parentheses(text):
    result = ""
    is_inside = False

    for x in range(len(text)):
        if text[x] == "(":            
            is_inside = True

        elif text[x] == " " and text[x-1] == ")":    
            is_inside = False

        elif is_inside == False:
            result += text[x]            

    return result.replace ("  "," ")
    
print(remove_parentheses('text')) 
