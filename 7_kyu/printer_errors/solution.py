def printer_error(s):
    count = 0
    for letter in s:
        
        if 'a' <= letter <= 'm': # checks if the letter is between  a to m 
            continue
            
        else:
            count += 1 # increases count if there is an error
    
    rate_of_error = str(count) + "/" + str(len(s)) # trying to assign the fraction of error as a STRING
    return rate_of_error
