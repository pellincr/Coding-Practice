package smallestNonexistingPositive;
import java.util.Arrays;
public class smallestNonexistingPositive {

	//purpose: to output the smallest psoitive number that does not exist in the array
	public static int smallestNoneistingPositive(int[] lon) {
		int res = 1;
		Arrays.sort(lon);
		int i = 0;
		while(i<lon.length) {
			if(lon[i]<=0) {i++;}
			else if(lon[i]>0 && lon[i] == res) {
				res++;
				i++;
			}
			else if(lon[i]>0 && lon[i] >res) {
				return res;
			}
		}
		return res;
	}
}
