package uniqueArrayProducts;

public class uniqueArrayProducts {

	//Purpose: to multiply all elements of the given array together
	public static int arrayProduct(int[] lon) {
		int res = 1;
		for(int num : lon) {
			res *= num;
		}
		return res;
	}
	
	//Purpose: to change each element in the given list to be the product of every element in the list
	//without including itself
	public static int[] uniqueArrayProduct(int[] lon) {
		int temp = arrayProduct(lon);
		int i = 0;
		while(i<lon.length) {
			lon[i] = temp/lon[i];
			i++;
		}
		return lon;
	}
}
