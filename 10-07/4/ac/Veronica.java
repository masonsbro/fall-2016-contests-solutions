import java.util.*;
import java.io.*;

public class Veronica {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int cases = Integer.parseInt(br.readLine());

		for (int a = 0; a < cases; a++) {
			String line = br.readLine();
			StringTokenizer st = new StringTokenizer(line);
			int numItems = Integer.parseInt(st.nextToken());
			int numTake = Integer.parseInt(st.nextToken());
			String[] items = new String[numItems];
			st = new StringTokenizer(br.readLine());
			for (int b = 0; b < items.length; b++) {
				items[b] = st.nextToken();
			}

			Map<String, Integer> inventory = new HashMap<String, Integer>();
			// First item we're including
			int start = -1;
			// Last item we're including
			int finish = -1;
			boolean done = false;
			int minTake = Integer.MAX_VALUE;

			while (!done) {
				// We have enough items, move start forward
				if (inventory.size() == numTake) {
					start++;
					// Off the end of the array
					if (start >= items.length) {
						done = true;
					} else {
						removeItem(items[start], inventory);
					}
				} else { // Not enough items, move finish forward
					finish++;
					if (finish >= items.length) {
						done = true;
					} else {
						addItem(items[finish], inventory);
					}
				}

				if (inventory.size() == numTake && finish - start < minTake) {
					minTake = finish - start;
				}
			}

			if (minTake == Integer.MAX_VALUE) {
				System.out.println(-1);
			} else {
				System.out.println(minTake);
			}
		}
	}

	private static void removeItem(String item, Map<String, Integer> map) {
		int currCount = map.get(item);
		currCount--;
		if (currCount == 0) {
			map.remove(item);
		} else {
			map.put(item, currCount);
		}
	}

	private static void addItem(String item, Map<String, Integer> map) {
		int currCount = 0;
		if (map.containsKey(item)) {
			currCount = map.get(item);
		}
		currCount++;
		map.put(item, currCount);
	}






}