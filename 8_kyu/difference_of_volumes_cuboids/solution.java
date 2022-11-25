public class CuboidVolumes {
  public static int findDifference(final int[] firstCuboid, final int[] secondCuboid) {
    int volume1 = 1;
    int volume2 = 1;
    
    for (int i = 0; i < firstCuboid.length; i++) {
      volume1 *= firstCuboid[i];
    }
    
    for (int j = 0; j < secondCuboid.length; j++) {
      volume2 *= secondCuboid[j];
    }
    
    
    return volume1 > volume2 ? volume1 - volume2 : volume2 - volume1;
  }
}
