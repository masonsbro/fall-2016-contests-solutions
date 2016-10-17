import java.util.*;
import java.io.*;

public class Solution {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int cases = Integer.parseInt(br.readLine());
		for (int a = 0; a < cases; a++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			int numBars = Integer.parseInt(st.nextToken());
			int maxWeight = Integer.parseInt(st.nextToken());
			Metal[] metals = new Metal[numBars];

			for (int b = 0; b < numBars; b++) {
				st = new StringTokenizer(br.readLine());
				int count = Integer.parseInt(st.nextToken());
				int weight = Integer.parseInt(st.nextToken());
				int value = Integer.parseInt(st.nextToken());
				metals[b] = new Metal(count, weight, value);
			}

			Arrays.sort(metals);
			int pos = 0;
			long value = 0;
			while (maxWeight > 0 && pos < metals.length) {
				long weightTaking = Math.min(maxWeight, metals[pos].getTaking());
				maxWeight -= weightTaking;
				value += (weightTaking * metals[pos].value);
				pos++;
			}

			System.out.println(value);
		}
	}

	private static class Metal implements Comparable<Metal> {
		private int numBars;
		private int weight;
		private int value;

		public Metal(int numBars, int weight, int value) {
			this.numBars = numBars;
			this.weight = weight;
			this.value = value;
		}

		public int compareTo(Metal other) {
			return other.value - this.value;
		}

		public int getTaking() {
			return weight * numBars;
		}
	}
}