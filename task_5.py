def cipher(text, shift):    
    result = ""   
    
    for letter in range(len(text)):         
        
        if ord(text[letter]) == 32:
                result += " "      
        elif text[letter].isupper():
            

            if ord(text[letter]) > 90 - shift:
                result += chr(ord(text[letter]) + shift - 26)    

            else:
                result += chr(ord(text[letter]) + shift)
   
        else:
                      

            if ord(text[letter]) > 122 - shift:
                result += chr(ord(text[letter]) + shift - 26)    

            else:
                result += chr(ord(text[letter]) + shift)
        
    
    return result
    

def decipher(text, shift):    
    result = ""   
    
    for letter in range(len(text)):
               

        if ord(text[letter]) == 32:
                result += " "      
        elif text[letter].isupper():            

            if ord(text[letter]) - shift < 65:
                result += chr(ord(text[letter]) - shift + 26)    

            else:
                result += chr(ord(text[letter]) - shift)
   
        else:
                      

            if ord(text[letter]) - shift < 97 :
                result += chr(ord(text[letter]) - shift + 26)    

            else:
                result += chr(ord(text[letter]) - shift)
        
    
    return result
