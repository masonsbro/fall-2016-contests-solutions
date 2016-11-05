import java.util.*;
import java.io.*;

public class Veronica {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int cases = Integer.parseInt(br.readLine());
		for (int a = 0; a < cases; a++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			int toCompare = Integer.parseInt(st.nextToken());
			String original = st.nextToken();
			int[] org = getColorArray(original);
			Color[] colors = new Color[toCompare];
			for (int b = 0; b < toCompare; b++) {
				String co = br.readLine();
				int[] curr = getColorArray(co);
				int diff = 0;
				for (int c = 0; c < curr.length; c++) {
					diff += (org[c] - curr[c]) * (org[c] - curr[c]);
				}
				colors[b] = new Color(co, diff);
			}
			Arrays.sort(colors);
			System.out.println("Case " + original + ":");
			for (Color c : colors) {
				System.out.println(c.stringRep);
			}
		}
	}

	public static int[] getColorArray(String original) {
		int[] org = new int[3];
		org[0] = Integer.parseInt(original.substring(1, 3), 16);
		org[1] = Integer.parseInt(original.substring(3, 5), 16);
		org[2] = Integer.parseInt(original.substring(5, 7), 16);
		return org;
	}

	private static class Color implements Comparable<Color> {
		String stringRep;
		int distance;

		public Color(String s, int distance) {
			this.stringRep = s;
			this.distance = distance;
		}

		public int compareTo(Color o) {
			if (o.distance == this.distance)
				return this.stringRep.compareTo(o.stringRep);
			else
				return this.distance - o.distance;
		}
	}
}