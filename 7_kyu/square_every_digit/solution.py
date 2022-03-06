def square_digits(num):
    squared = "" 
    for digit in str(num): # you can't iterate through an integer so you convert it to a string
        squared += str(int(digit)**2) #turn the digit back into an int and square it then turn it into a string again so you can concatenate it
    return int(squared) #turn it back to an integer otherwise the results will flag false since it is a string
