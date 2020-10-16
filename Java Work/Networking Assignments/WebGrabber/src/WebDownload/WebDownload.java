package WebDownload;
import java.net.Socket;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.io.PrintWriter;
public class WebDownload {

	public static void send(PrintWriter out, String msg)
	{
		out.print(msg + "\r\n");
	}

	private static void sendHTTPCode(PrintWriter out, String file, String host)
	{
		send(out, "GET " + file + " HTTP/1.1");
		send(out, "HOST: " + host);
		send(out, "");
		out.flush();
	}
	
	private static void receiveHTTPData(BufferedReader in) throws Exception
	{
		String line = in.readLine();
		do
		{
			System.out.println("Got: " + line);
			line = in.readLine();
		}
		while (line != null);
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		System.out.println("This program will download an arbitrary webpage");
		// the host to connect to:
		String host = "sciris.shu.edu";
		// the port to use for the connection
		int port = 80;
		// the file to get
		String file = "/";
		if (args.length == 2)
			file = args[1];
			if (args.length >= 1)
			host = args[0];
			else
			{
			System.out.println("Usage: java WebGrabber host [file]");
			     	System.exit(-1);
			}

			// setting u the streams etc. 

		Socket s;
		try {
			
			//Connecting...
			System.out.println("Connecting to " + host + " on port " + port);
			s = new Socket(host, port);
			
			System.out.println("Connection established: \n" + s);


			System.out.println("Setting up input and output streams of characters");
			BufferedReader in = new BufferedReader(
					new InputStreamReader(
							s.getInputStream()));

			PrintWriter out = new PrintWriter(
					new OutputStreamWriter(
							s.getOutputStream()));
			
			sendHTTPCode(out,file,host);
			receiveHTTPData(in);
			// here I can send out a character through the socket using 
			// out.println(). However, there is a subtle problem: depending on the 
			// implementation of the PrintWriter class, it appends a different line
			// ending to the end of the string. In Unix, lines will end with a '\n' 
			// control character, while in Windows, the line end is signified by 
			// "\r\n" (also called CR (Carriage Return) + LF (Line Feed). To ensure
			// that your program works the same on Windows and Unix, always create your
			// own local method to properly terminate a 'line' of characters to send out.
			// Here we create the "send" method for just this purpose.

			in.close();
			out.close();
			s.close();
			System.out.println("Disconneted");

		} catch (Exception e) {

			System.err.println("Error: " + e);
		}
	}
}
