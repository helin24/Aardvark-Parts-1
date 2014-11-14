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
}
