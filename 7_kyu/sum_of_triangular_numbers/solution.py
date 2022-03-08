def sum_triangular_numbers(n):
    sum = 0
    for num in range(1, n+1):
      sum += num*(num+1)/2; # used the formula of the sum of triangular numbers online so I can find the sum 
    return sum;
