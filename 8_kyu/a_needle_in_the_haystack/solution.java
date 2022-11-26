public class Kata {
  public static String findNeedle(Object[] haystack) {
    for (int i = 0; i < haystack.length; i++) {
      if (haystack[i] == "needle") {
        return String.format("found the needle at position %d", i);
      }
    }
    return "no needle :(";
  }
}
