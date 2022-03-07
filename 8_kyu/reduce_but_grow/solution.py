def grow(arr):
    multiply = 1
    for num in arr:
        multiply = multiply * num # assigning a new value each time multiply is multiplied by the next number in the array
    return multiply
