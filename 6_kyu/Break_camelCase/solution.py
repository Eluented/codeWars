def solution(s):
    
    # made a variable to add to
    sol = ""
    
    # loops through the string with index
    for i in range(len(s)):
        
        # if the letter is NOT a capital latter - add it onto the empty string
        if s[i] != s[i].upper():
            sol += s[i]
            
        # ELSE - add a space and add the capital letter
        else:
            sol += " " + s[i]
            
    return sol
