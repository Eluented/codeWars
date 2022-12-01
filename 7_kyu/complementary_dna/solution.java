public class DnaStrand {
  public static String makeComplement(String dna) {
    String dnaReturn = "";
    
    for (int i = 0; i < dna.length(); i++) {
      if (dna.charAt(i) == 'A') {
        dnaReturn += 'T';
      } if (dna.charAt(i) == 'T') {
        dnaReturn += 'A';
public class DnaStrand {
  public static String makeComplement(String dna) {
    String dnaReturn = "";
    
    for (int i = 0; i < dna.length(); i++) {
      if (dna.charAt(i) == 'A') {
        dnaReturn += 'T';
      } if (dna.charAt(i) == 'T') {
        dnaReturn += 'A';
      } if (dna.charAt(i) == 'C') {
        dnaReturn += 'G';
      } if (dna.charAt(i) == 'G'){
        dnaReturn += 'C';
      }
    }
    return dnaReturn;
  }
}
