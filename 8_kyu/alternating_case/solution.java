public class StringUtils {
  
  public static String toAlternativeString(String string) {
    String alternatingCase = "";
    
    for (int i = 0; i < string.length(); i++) {
      char currentCharacter = string.charAt(i);
      
      if (Character.isUpperCase(currentCharacter)) {
        alternatingCase += Character.toLowerCase(currentCharacter);
      } else {
        alternatingCase += Character.toUpperCase(currentCharacter);
      }
    }
    return alternatingCase;
  }
}
