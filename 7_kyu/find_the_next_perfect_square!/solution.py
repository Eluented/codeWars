import math
def find_next_square(sq):
    previous_square = math.isqrt(sq)
    if (previous_square ** 2 == sq): # checking if the number is a perfect square 
        return (previous_square + 1)**2  #  adding 1 to the previous square and then finding the next perfect square
    else:
        return -1 # return -1 if not a perfect square 
