package Processing;

public class FCFS {

	
	//Purpose: to print the FCFS Gnatt chart
	public static String FCFSGnatt(Process[] pl)
	{
		String res = FCFSProcessOrder(pl) + "\n" + FCFSProcessTiming(pl);
		return res;
	}
	
	//Purpose: to print the names of each process in the FCFS gnatt chart
	public static String FCFSProcessOrder(Process[] pl)
	{
		String res = "";
		for(int i = 0; i<pl.length;i++)
		{
			res += "   " +pl[i].getName() + "\t";
		}
		return res;
	}
	
	//Purpose: to print the times for the FCFS gnatt chart
	public static String FCFSProcessTiming(Process[] pl)
	{
		String res = "0";
		int nextTime = 0;
		for(int i = 0; i<pl.length; i++)
		{
			nextTime += pl[i].getBT();
			res+= "------" + nextTime;
			
			
		}
		return res;
	}
	
	//Purpose: to run the list of process under the FCFS method
	public static Process[] FirstComeFirstServed(Process[] pl)
	{
		Process[] res;
		Process[] temp = pl;
		insertionSortArrive(temp);
		res = new Process[temp.length];
		int prevTotalBT = 0;
		int i = 0;
		while(i<temp.length)
		{
			
			res[i] = temp[i];
			res[i].setST(prevTotalBT);
			prevTotalBT += res[i].getBT();
			res[i].setCT(prevTotalBT);
			res[i].setWT(res[i].calcWT());
			res[i].setTT(res[i].calcTT());

			
			i++;
		}
		
		return res;
	}
	
	//Purpose: to sort the given array by each process' arrival time
	public static void insertionSortArrive(Process[] pl) {
	    for (int i = 1; i < pl.length; i++) {
	        Process current = pl[i];
	        int j = i - 1;
	        while(j >= 0 && current.getAT() < pl[j].getAT()) {
	            pl[j+1] = pl[j];
	            j--;
	        }
	        pl[j+1] = current;
	    }
	}
}

