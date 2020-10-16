package Processing;

public class SJF {

	//Purpose: to output the gnatt chart
	public static String SJFGnatt(Process[] pl)
	{
		String res = SJFProcessOrder(pl) + "\n" + SJFProcessTiming(pl);
		return res;
	}
	
	//Purpose: to output the names of each process in the gantt chart
	public static String SJFProcessOrder(Process[] pl)
	{
		String res = "";
		for(int i = 0; i<pl.length;i++)
		{
			res += pl[i].getName() + "\t";
		}
		return res;
	}
	
	//Purpose: to output the times of each process in the gnatt chart
	public static String SJFProcessTiming(Process[] pl)
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
	
	//Purpose: to run the list of processes under the SJF method
	public static Process[] ShortestJobFirst(Process[] pl)
	{
		Process[] sorted = pl;
		insertionSortArrive(sorted);
		Process[] res = sorted;
		int ctr = 0;
		int prevTotalBT = 0;
		int i = indexofSmallestBurst(sorted, prevTotalBT);
		while(ctr<sorted.length)
		{
			sorted[i].setST(prevTotalBT);
			prevTotalBT += sorted[i].getBT();
			sorted[i].setCT(prevTotalBT);
			sorted[i].setWT(sorted[i].calcWT());
			sorted[i].setTT(sorted[i].calcTT());
			ctr++;
			res[i] = sorted[i];
			sorted = removeElement(sorted, sorted[i]);
			i = indexofSmallestBurst(sorted, prevTotalBT);
		}
		
		return res;
	}
	
	//Purpose: to remove the element in the given array by replacing it with a non-existant vector
	public static Process[] removeElement(Process[] pl, Process p)
    {
        if(pl == null)
        {
            return pl;
        }
        else {
            Process[] res;
            res = new Process[pl.length];
            for(int i = 0; i<pl.length;i++)
            {
                if(pl[i]!=p)
                {
                    res[i] = pl[i];
                }
                else {
                	res[i] = new Process("Non-Existant", 999999999,99999999);
                }
            }
            return res;
        }
    }
	
	//Purpose: to get the index of the process with the smallest arrival time
	//Assumption: the given array is sorted by arrival time
	public static int indexofSmallestBurst(Process[] pl, int time)
	{
		int currentSmallest = 0;
		for(int i = 1; i<pl.length;i++)
		{
			if((pl[i].getBT()<pl[currentSmallest].getBT()) && (pl[i].getAT()<= time))
			{
				currentSmallest = i;
				}
		}
		return currentSmallest;
	}
	
	
	//Purpose: to sort the given array by each process' burst time
	public static void insertionSortBurst(Process[] pl) {
	    for (int i = 1; i < pl.length; i++) {
	        Process current = pl[i];
	        int j = i - 1;
	        while(j >= 0 && current.getBT() < pl[j].getBT()) {
	            pl[j+1] = pl[j];
	            j--;
	        }
	        pl[j+1] = current;
	    }
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
