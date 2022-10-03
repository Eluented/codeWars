def to_weird_case(string):
    final_string = []
    
    splitString = string.split()
    
    for word in splitString:
        helper_string = ""
        
        for idx, letter in enumerate(word):
            if (idx % 2 != 0):
                helper_string += letter
            else: 
                helper_string += letter.upper()
                
        final_string.append(helper_string)
        
    return " ".join(final_string)
