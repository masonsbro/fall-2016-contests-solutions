import java.util.*;
import java.io.*;

public class Solution {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int cases = Integer.parseInt(br.readLine());
		assert (cases >= 1 && cases <= 10);
		for (int caseNum = 1; caseNum <= cases; caseNum++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			int numItems = Integer.parseInt(st.nextToken());
			long goalExcitement = readDouble(st.nextToken());
			long maxExcitement = readDouble(st.nextToken());
			long budget = readDouble(st.nextToken());

			Piece[] pieces = new Piece[numItems];
			for (int b = 0; b < numItems; b++) {
				st = new StringTokenizer(br.readLine());
				String name = st.nextToken();
				long excitement = readDouble(st.nextToken());
				long cost = readDouble(st.nextToken());
				pieces[b] = new Piece(name, excitement, cost);
			}

			TreeMap<Integer, TreeSet<String>> result = new TreeMap<>();
			Coaster coaster = new Coaster();
			findCoasters(goalExcitement, maxExcitement, budget, pieces, coaster, result);
			System.out.println("CASE: " + caseNum);
			StringBuilder sb = new StringBuilder();
			if (result.size() == 0) {
				System.out.println("IMPOSSIBLE\n");
			} else {
				for (Integer count : result.keySet()) {
					TreeSet<String> thisTime = result.get(count);
					for (String s : thisTime) {
						sb.append(s);
						sb.append('\n');
					}
				}
				System.out.println(sb.toString());
			}
		}
	}

    private static long readDouble(String input) {
        return Long.parseLong(input.substring(0, input.length() - 3) +
                input.substring(input.length() - 2, input.length()));
    }

	private static void findCoasters(long goalExcitement, long maxExcitement, long budget, Piece[] pieces, 
				Coaster coaster, TreeMap<Integer, TreeSet<String>> result) {
		if (coaster.excitement == goalExcitement) {
			if (!result.containsKey(coaster.pieces.size()))
				result.put(coaster.pieces.size(), new TreeSet<String>());
			result.get(coaster.pieces.size()).add(coaster.toString());
		}

		for (int index = 0; index < pieces.length; index++) {
			if (coaster.cost + pieces[index].cost <= budget 
					&& coaster.excitement + pieces[index].excitement <= maxExcitement) {
				coaster.addPiece(pieces[index]);
				findCoasters(goalExcitement, maxExcitement, budget, pieces, coaster, result);
				coaster.removeLastPiece();
			}
		}
	}

	private static class Coaster {
		private ArrayList<Piece> pieces;
		private long cost;
		private long excitement;

		public Coaster() {
			pieces = new ArrayList<Piece>();
			cost = 0;
			excitement = 0;
		}

		public String toString() {
			StringBuilder sb = new StringBuilder();
			for (int a = 0; a < pieces.size() - 1; a++) {
				sb.append(pieces.get(a).toString());
				sb.append(" -> ");
			}
			sb.append(pieces.get(pieces.size() - 1).toString());
			return sb.toString();
		}

		public void addPiece(Piece piece) {
			this.pieces.add(piece);
			this.cost += piece.cost;
			this.excitement += piece.excitement;
		}

		public void removeLastPiece() {
			Piece toRemove = pieces.get(pieces.size() - 1);
			pieces.remove(pieces.size() - 1);
			this.cost -= toRemove.cost;
			this.excitement -= toRemove.excitement;
		}
	}

	private static class Piece {
		private String name;
		private long excitement;
		private long cost;

		public Piece(String name, long excitement, long cost) {
			this.name = name;
			this.excitement = excitement;
			this.cost = cost;
		}

		public String toString() {
            //return String.format("(%s, %d, %d)", name, excitement, cost);
			return name;
		}
	}
}
