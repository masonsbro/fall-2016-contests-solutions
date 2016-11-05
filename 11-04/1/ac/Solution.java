import java.util.*;
import java.io.*;

public class Solution {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		Set<String> disallowed = 
				new HashSet<String>(Arrays.asList("pin", "pins", "pinned", "pinning", "pinner", "pinners"));
		int cases = Integer.parseInt(br.readLine());
		for (int a = 0; a < cases; a++) {
			String line = br.readLine();
			line = line.toLowerCase();
			StringTokenizer st = new StringTokenizer(line);
			int score = 0;
			while (st.hasMoreTokens()) {
				String word = st.nextToken();
				if (!disallowed.contains(word) && word.indexOf("pin") > -1) {
					score++;
				}
			}
			System.out.println(score);
		}
	}
}