def sum_of_minimums(numbers):
    total = 0
    
    for array in numbers:  # loop through each list in the nested list
        total += min(array) # add the minimum value in each list into total
    
    return total
        
