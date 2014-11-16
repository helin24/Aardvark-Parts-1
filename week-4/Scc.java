import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class Scc {
	static BufferedReader file;

	public static void main(String filename) {
		getFile(filename);
	}	
	
	public static BufferedReader getFile(String filename) {
		try
		{
			file = new BufferedReader(new FileReader(filename));	
		}
		catch(IOException e)
		{
			e.printStackTrace();
		}
		return file;
	}

	// Go backwards in graph
		// for each number 1.. end of graph vertices
			// check for vertices that connect to it 
			// if vertex has already been found then ignore
			// if vertex is new then check for vertices that connect
}
