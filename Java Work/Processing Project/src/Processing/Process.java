package Processing;
import java.util.Scanner;

//Authors: Craig Pelling and Anthony Mauro

//For some reason the gnatt chart for SRTF does not work outside of the actual SRTF class itself, so in order to view it
//Please go to that class and input the values again. The tables with the calculations exists here, only the chart is in
//SRTF class itself
public class Process {

	private String name; //process name
	private int BT; //Burst Time
	private int WT; //Wait Time
	private int TT; // Turnaround Time
	private int AT; // Arrival Time
	private int ST; // Start Time
	private int CT; // Completion Time
	
	public Process(String n, int b, int a)
	{
		name = n;
		BT = b;
		WT = 0;
		TT = 0;
		AT = a;
		ST = 0;
		CT = 0;
	}
	
	//Purpose: observer for the name of the process
	public String getName() {
		return this.name;
	}
	
	//Purpose: to change the name of this process
	public void setName(String s)
	{
		this.name = s;
	}
	
	//Purpose: observer for the Burst Time of the process
	public int getBT() {
		return this.BT;
	}
	
	//Purpose: to change the Burst Time of this process
	public void setBT(int b)
	{
		this.BT = b;
	}
	
	//Purpose: observer for the Wait Time of the process
	public int getWT() {
		return this.WT;
	}
	
	//Purpose: to change the wait time of this process
	public void setWT(int w)
	{
		this.WT = w;
	}
	
	
	//Purpose: observer for the Turnaround Time of the process
	public int getTT() {
		return this.TT;
	}
	
	//Purpose: to change the Turnaround Time of this process
	public void setTT(int t)
	{
		this.TT = t;
	}
	
	//Purpose: observer for the Arrival Time of the process
	public int getAT() {
		return this.AT;
	}
	
	//Purpose: to change the arrival time of this process
	public void setAT(int a)
	{
		this.AT = a;
	}
	
	//Purpose: observer for the Start Time of the process
	public int getST()
	{
		return this.ST;
	}
	
	//Purpose: to change the Start Time for this process
	public void setST(int s)
	{
		this.ST = s;
	}
	
	//Purpose: observer for the Completion Time of the process
	public int getCT()
	{
		return this.CT;
	}
	
	//Purpose: to change the Completion Time for this process
	public void setCT(int c)
	{
		this.CT = c;
	}
	
	//Purpose: to calculate the wait time of this process
	public int calcWT()
	{
		return this.getST() - this.getAT();
	}
	
	//purpose: to calculate the turnaround time of this process
	public int calcTT()
	{
		return this.getCT() - this.getAT();
	}
	
	//Purpose: converts this process to a string
	public String toString() {
		return this.name +"\t   "+  this.BT +"\t\t  "+ this.WT + "\t\t"+  this.TT + "\t\t\t" + this.AT;
	}
	
	//Purpose: converts this array list of process to strings
	public static String toStringList(Process[] pl) {
		String res = "";
		int i = 0;
		while(i<pl.length)
		{
			res += pl[i].toString() +"\n";
			i++;
		}
		return res;
	}


	//Purpose: to output the tables and gnatt charts of all methods run on the input list of processes
	//except for the SRTF gnatt chart for whatever reason(go to SRTF class to view it)
	public static void main(String[] args)
	{
		String top = "Process\t   Burst Time\t  Wait Time\tTurnaround Time\t\tArrival Time";
		
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
		System.out.println("FCFS-");
		System.out.println(top);
		System.out.println(toStringList(FCFS.FirstComeFirstServed(pl)));
		System.out.println();
		System.out.println("FCFS Gnatt Chart-");
		System.out.println(FCFS.FCFSGnatt(FCFS.FirstComeFirstServed(pl)));
		System.out.println();
		System.out.println();
		System.out.println("SJF-");
		System.out.println(top);
		System.out.println(toStringList(SJF.ShortestJobFirst(pl)));
		System.out.println();
		System.out.println("SJF Gnatt Chart-");
		System.out.println(SJF.SJFGnatt(SJF.ShortestJobFirst(pl)));
		System.out.println();
		System.out.println();
		System.out.println("SRTF-");
		System.out.println(top);
		System.out.println(toStringList(SRTF.ShortestRemainingTimeFirst(pl)));
	}
}
