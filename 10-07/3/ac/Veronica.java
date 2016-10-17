import java.util.*;
import java.io.*;

public class Veronica {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int cases = Integer.parseInt(br.readLine());
		for (int z = 0; z < cases; z++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			int m = Integer.parseInt(st.nextToken());
			int n = Integer.parseInt(st.nextToken());
			int[] i = new int[m];
			st = new StringTokenizer(br.readLine());
			int lastI = Integer.parseInt(st.nextToken());
			for (int b = 0; b < i.length; b++) {
				int t = Integer.parseInt(st.nextToken());
				i[b] = t - lastI;
				lastI = t;
			}
			ArrayList<Integer> a = new ArrayList<Integer>();
			ArrayList<Integer> j = new ArrayList<Integer>();
			st = new StringTokenizer(br.readLine());
			StringTokenizer st2 = new StringTokenizer(br.readLine());
			while (st.hasMoreTokens()) {
				a.add(Integer.parseInt(st.nextToken()));
				j.add(Integer.parseInt(st2.nextToken()));
			}

			StringBuilder result = new StringBuilder();
			int index = 0;
			for (int row = 0; row < m; row++) {
				for (int col = 0; col < n; col++) {
					if (i[row] != 0 && j.get(index) == col) {
						result.append(a.get(index) + " ");
						index++;
						i[row]--;
					} else {
						result.append("0 ");
					}
				}
				result.deleteCharAt(result.length() - 1);
				result.append('\n');
			}
			result.deleteCharAt(result.length() - 1);

			System.out.println(result.toString());
		}
	}
}