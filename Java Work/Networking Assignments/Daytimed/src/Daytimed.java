/* Craig Pelling
 * CSAS 3211
 * The purpose of this program is to run a server that displays the current date and time when a client is conencted
 */

import java.io.IOException;
import java.io.OutputStreamWriter;
import java.io.PrintWriter;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.Date;
public class Daytimed {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int port = 1301;
		ServerSocket server;
		try {
			server = new ServerSocket(port);
			System.out.println("Server setup, waiting: " + server);
			
			boolean running = true;
			while (running)
			{
			// Code to wait for incoming connection and for handling it goes inside the loop, i.e.
			// everything from Socket client = server.accept() up to but excluding the line server.close()
				Socket client = server.accept();
				System.out.println("Client connected: " + client);
				
				PrintWriter out = new PrintWriter(
						new OutputStreamWriter(
								client.getOutputStream()));
						
				Date today = new Date();
				out.println(today);
				out.flush();
				// code to setup input & output steams to communicate with the client goes here
				client.close();
			}
			
			server.close();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
}
