def div_con(x):
    sum_of_string = 0
    non_string = 0
    for i in x:
        
        if (i == str(i)):
            sum_of_string += int(i); #checks if its a string - converts it to an int and adds it to the sum of string
            
        if (i == int(i)):
            non_string += i # checks if its an int - just adds it to the non_string sum
            
    
    return non_string - sum_of_string # subtract the sum of string from the non string total and you get the answer!
