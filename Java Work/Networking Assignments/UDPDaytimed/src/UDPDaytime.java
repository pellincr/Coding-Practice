//Craig Pelling
//CSAS 3211
//Class for the Client
import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.InetAddress;
import java.net.ServerSocket;
import java.net.SocketException;
import java.util.Scanner;
public class UDPDaytime {

	public static void main(String[] args)
	{
		Scanner input = new Scanner(System.in);
		System.out.println("What port would you like to connect to? ");
		int port = input.nextInt();
		input.close();
		// Embed the following code in a try-catch block
		// Define host and port (preferably from the command line arguments)
		// Creates new DatagramSocket that listens on an arbitrary port. Note:
		// Using 0 as port binds the DatagramSocket to first available port 
		DatagramSocket s;
		
		try {
			s = new DatagramSocket(0);
			// Allows the client to timeout if it waits
			// for too long. (5 seconds)
			s.setSoTimeout(5000);
			
			System.out.println("Client setup, waiting: " + s);
			//Gets the local IP
			String host = InetAddress.getLocalHost().getHostName();;
			sendRequest(s, host, port);
			waitForDate(s);
			s.close();
		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
	private static void sendRequest(DatagramSocket s, String host, int port)
			throws Exception
	{
		// Get the host address as an InetAddress, using static method getByName
		// Create a datagram packet for sending (arbitrary) data to address on port
		// Sending datagram
		InetAddress address = InetAddress.getByName(host);
		byte[] data = new byte[1];
		DatagramPacket packet = new DatagramPacket(data, data.length, address, port);
		s.send(packet);

	}
	private static void waitForDate(DatagramSocket s) throws Exception
	{
		// Create a datagram packet for receiving data of length data.length
		// Wait for incoming datagram packet (which will contain the date/time)
		// Decode the data received in the datagram and print it out
		byte[] buffer = new byte[256];
		DatagramPacket packet = new DatagramPacket(buffer, buffer.length);
		s.receive(packet);
		String today = new String(packet.getData());
		System.out.println(today);
	}

}
