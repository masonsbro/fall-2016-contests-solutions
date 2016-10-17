import java.util.*;
import java.io.*;

public class Solution {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		int cases = Integer.parseInt(br.readLine());
		for (int a = 0; a < cases; a++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			int numEscalators = Integer.parseInt(st.nextToken());
			int numFloors = Integer.parseInt(st.nextToken());
			int numHeroes = Integer.parseInt(st.nextToken());

			HashMap<Integer, Node> graph = new HashMap<Integer, Node>();

			for (int b = 0; b < numFloors; b++) {
				graph.put(b, new Node(b));
			}

			for (int b = 0; b < numEscalators; b++) {
				st = new StringTokenizer(br.readLine());
				int speed = Integer.parseInt(st.nextToken());
				int div = Integer.parseInt(st.nextToken());
				String direction = st.nextToken();
				if (direction.equals("DOWN")) {
					for (int c = div; c < numFloors; c += div) {
						Node first = graph.get(c);
						Node second = graph.get(c - div);
						Edge secondToFirst = new Edge(second, first, div * speed);
						second.connections.add(secondToFirst);
					}
				} else if (direction.equals("UP")) {
					for (int c = div; c < numFloors; c += div) {
						Node first = graph.get(c);
						Node second = graph.get(c - div);
						Edge firstToSecond = new Edge(first, second, div * speed);
						first.connections.add(firstToSecond);
					}
				} else {
					throw new IllegalArgumentException(direction + " is not a direction");
				}
			}

			djikstra(graph, numFloors);

			StringTokenizer heroes = new StringTokenizer(br.readLine());
			int max = Integer.MIN_VALUE;
			boolean unreachable = false;
			for (int b = 0; b < numHeroes && !unreachable; b++) {
				int currHero = Integer.parseInt(heroes.nextToken());
				if (graph.get(currHero).visited == false) {
					unreachable = true;
				}
				else if (graph.get(currHero).cost > max)
					max = graph.get(currHero).cost;
			}

			if (unreachable)
				System.out.println("IMPOSSIBLE");
			else
				System.out.println(max);
		}
	}

	private static void djikstra(HashMap<Integer, Node> graph, int numFloors) {
		Node start = graph.get(numFloors - 1);
		PriorityQueue<Node> toVisit = new PriorityQueue<Node>();
		start.cost = 0;
		toVisit.add(start);

		while (!toVisit.isEmpty()) {
			Node current = toVisit.remove();
			current.visited = true;

			for (Edge connection : current.connections) {
				Node end = connection.end;
				int newCost = current.cost + connection.weight;
				if (!end.visited && newCost < end.cost) {
					end.cost = newCost;
					toVisit.add(end);
				}
			}
		}
	}

	private static class Node implements Comparable<Node> {
		private HashSet<Edge> connections;
		private int floor;
		private int cost;
		private boolean visited;

		public Node(int floor) {
			this.floor = floor;
			connections = new HashSet<Edge>();
			visited = false;
			cost = Integer.MAX_VALUE;
		}

		public int compareTo(Node other) {
			return this.cost - other.cost;
		}

		public String toString() {
			return (floor + " " + cost);
		}
	}

	private static class Edge {
		private Node start;
		private Node end;
		private int weight;

		public Edge(Node start, Node end, int weight) {
			this.start = start;
			this.end = end;
			this.weight = weight;
		}

		public String toString() {
			return "START " + start.floor + " FINISH " + end.floor + " WEIGHT " + weight;
		}
	}
}