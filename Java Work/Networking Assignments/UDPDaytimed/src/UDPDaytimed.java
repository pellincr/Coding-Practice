//Craig Pelling
//CSAS 3211
//Class for the Server
import java.net.ServerSocket;
import java.net.SocketException;
import java.util.Date;
import java.net.DatagramSocket;
import java.net.InetAddress;
import java.net.DatagramPacket;
import java.util.Scanner;
public class UDPDaytimed {



	public static void main(String[] args)
	{
		Scanner input = new Scanner(System.in);
		System.out.println("What port would you like to connect to? ");
		int port = input.nextInt();
		input.close();
		// Embed the following code in a try-catch block
		// Define port to listen on (preferably from the command line arguments)
		// Create a new DatagramSocket that listens to the specified port. 
		DatagramSocket s;
		try {
			s = new DatagramSocket(port);
			System.out.println("Server runnning");
			// Embed the following code in an infinite loop
			boolean running = true;
			while(running) {
				DatagramPacket teaser = waitForTeaser(s);
				// extract client InetAdress and port that client listens to
				sendDate(s, teaser.getAddress(), teaser.getPort());
				// end of loop
			}
			s.close();
		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}

	private static DatagramPacket waitForTeaser(DatagramSocket s) throws Exception
	{
		// Create a datagram packet for receiving arbitrary data 
		// Wait for incoming datagram packet
		// return the incoming datagram packet
		byte[] buffer = new byte[256];
		DatagramPacket packet = new DatagramPacket(buffer, buffer.length);
		s.receive(packet);
		return packet;
	}

	private static void sendDate(DatagramSocket s, InetAddress client, int port) throws Exception
	{
		// Create data, an array of bytes encoding today's date & time
		// Create a datagram packet for sending encoded data to client on port
		// Sending datagram to client on port
		Date today = new Date();
		byte[] data = today.toString().getBytes();
		DatagramPacket packet = new DatagramPacket(data, data.length, client, port);
		s.send(packet);
	}

}
