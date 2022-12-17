public class Correct {
  public static String correct(String string) {
    String correctString = "";
    
    for (int i = 0; i < string.length(); i++) {
      if (string.charAt(i) == '5'){
        correctString += 'S';
      } else if (string.charAt(i) == '0') {
        correctString += 'O';
      } else if (string.charAt(i) == '1') {
        correctString += 'I';
      } else {
        correctString += string.charAt(i);
      }
    }
    return correctString;
  }
}
