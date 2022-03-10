def repeater(string, n):
    repetition = "" # empty string to be used for concatenating the amount of repetitions 
    
    for x in range(n):
        repetition += string # concatenating the empty string with the string that was passed in the argument 
    
    return repetition
