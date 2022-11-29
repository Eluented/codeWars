public class Factorial {

  public int factorial(int n) {
    // Happy coding :-)
    if (n < 0 || n > 12) {
      throw new IllegalArgumentException();
    } else if (n == 0) {
      return 1;
    }
    
    int sum = 1;
    
    for (int i = 1; i <= n; i++) {
      sum *= i;  
    }
    
    return sum;
  }
}
