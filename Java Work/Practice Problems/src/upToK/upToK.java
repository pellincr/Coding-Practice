package upToK;

public class upToK {

	
	//Purpose: to determine if there are any 2 ints in the given list that add up to K
	public static boolean addUpToK(int k, int[] lon) {
		int i = 0;
		int j = 0;
		while(i<lon.length) {
			while(j<lon.length) {
				if(i==j) {j++;}
				else if (lon[i] + lon[j] == k) {return true;}
				else {j++;}
			}
			i++;
		}
		return false;
	}
}
