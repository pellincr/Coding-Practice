package Processing;

import java.util.Scanner;

public class SRTF {

	//Purpose: to create the gnatt chart for SRTF(only works inside this class for some reason)
	public static String SRTFGnatt(Process[] pl)
	{
        String res1 =  "";
        Process[] sorted = pl;
        insertionSortArrive(sorted);
        int i1 = indexofSmallestBurst(sorted, 0);
        int totalTime = totalBT(sorted);
        for (int NextTick = 1; NextTick <= totalTime; NextTick++)
        {
            res1 += sorted[i1].getName() + "  ";
            sorted[i1] = new Process(sorted[i1].getName(), sorted[i1].getBT()-1, sorted[i1].getAT());
            if(sorted[i1].getBT() == 0)
            {
            	sorted = removeElement(sorted, sorted[i1]);
            }
            i1 = indexofSmallestBurst(sorted, NextTick);
        }
		
    	String res2 = "0";
    	int i2 = 1;
    	while(i2<=totalTime)
    	{
    		res2+="--" + i2;
    		i2++;
    	}
		String res3 = res1 + "\n" + res2;
		return res3;
	} 
 
	//Purpose: to run the the list of the process under the SRTF method
	public static Process[] ShortestRemainingTimeFirst(Process[] pl) {
		insertionSortArrive(pl);
		Process[] sorted = pl; //the sorted array by arrival time
		Process[] res = reset(copyProcess(pl)); //the resultant array		
		int i = indexofSmallestBurst(sorted, 0);//index of the current smallest burst time that is available
		int totalTime = totalBT(pl);//the total burst time for the array of processes
		int clock = 0;
		while(clock < totalTime)//will loop through process 1 tick at a time until each process is done
		{
			clock++;//Increments clock tick indicating how many process will have been ran
			sorted[i] = new Process(sorted[i].getName(), sorted[i].getBT()-1, sorted[i].getAT());//decrements the BT of the process by 1 to get closer to finishing
			if(sorted[i].getBT() == 0)//Begin calculations if the process has finished
			{
				res[i].setCT(clock);
				sorted = removeElement(sorted, sorted[i]);
				res[i].setTT(res[i].calcTT());
				res[i].setWT(res[i].getTT()-res[i].getBT());
			}			
			i = indexofSmallestBurst(sorted, clock);
		}
		return res;
	}
	
	//Purpose: to copy a given array of processes
	public static Process[] copyProcess(Process[] pl)
	{
		Process[] res = new Process[pl.length];
		for(int i = 0; i<pl.length;i++)
		{
			res[i] = pl[i];
		}
		return res;
	}
	
	//Purpose: to reset the WT and TT of the given array of processes 
	public static Process[] reset(Process[] pl) {
		Process[] res = pl;
		for(int i = 0; i<pl.length;i++)
		{
			res[i].setTT(0);
			res[i].setWT(0);
		}
		return res;
	}
	
	//Purpose: to calculate the total burst time for the given array of processes
	public static int totalBT(Process[] pl)
	{
		int sum = 0;
		for(int i =0; i<pl.length; i++)
		{
			sum+= pl[i].getBT();
		}
		return sum;
	}
	
	//Purpose: to remove the process p from the given array pl by replacing it with a non-existant process
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
	
	
	//Purpose: to provide the gnatt chart for SRTF
	public static void main(String[] args)
	{
		Scanner scanner = new Scanner(System.in);
		System.out.println("Enter the number of process you wish to operate on: ");
		int size = scanner.nextInt();
		Process[] pl = new Process[size]; 
		int i = 0;
		int pNumber = 1;
		while(i<size) {
			System.out.println("Enter Name of Process"+ pNumber+ ": ");
			String pName = scanner.next();
			System.out.println("Enter Burst Time of Process"+ pNumber+ ": ");
			int pBurst = scanner.nextInt();
			System.out.println("Enter Arrival Time of Process"+ pNumber+ ": ");
			int pArrive = scanner.nextInt();
			pNumber++;
			pl[i] = new Process(pName,pBurst,pArrive);
			i++;
		}
		System.out.println("SRTF Gnatt Chart-");
		System.out.println(SRTFGnatt(ShortestRemainingTimeFirst(pl)));
	}
}
