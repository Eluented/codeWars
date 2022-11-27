import java.util.Arrays;

public class Kata
{
    public static int expressionsMatter(int a, int b, int c)
    {
      int arr[] = {(a + b) * c, a * (b + c), a * b * c, a + b + c};
      int max = Arrays.stream(arr).max().getAsInt();
      
      return max;  
    }
}
