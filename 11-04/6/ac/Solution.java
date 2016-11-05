import java.io.*;
import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int T = scan.nextInt();
        while (T-- > 0) {
            int n = scan.nextInt();
            List<Integer> b = new ArrayList<Integer>();
            for (int i = 0; i < n; i++) {
                b.add(scan.nextInt());
            }

            Queue<State> queue = new LinkedList<State>();
            Set<State> visited = new HashSet<State>();

            queue.add(new State(0, 0, 0));
            visited.add(new State(0, 0, 0));
            int ans = Integer.MAX_VALUE;

            while (!queue.isEmpty()) {
                State current = queue.remove();

                if (current.index == n) {
                    ans = Math.min(ans,
                            Math.abs(current.leftSum - current.rightSum));
                } else {
                    State leftState = new State(current.index + 1,
                            current.leftSum + b.get(current.index),
                            current.rightSum);
                    State rightState = new State(current.index + 1,
                            current.leftSum,
                            current.rightSum + b.get(current.index));

                    if (!visited.contains(leftState)) {
                        visited.add(leftState);
                        queue.add(leftState);
                    }

                    if (!visited.contains(rightState)) {
                        visited.add(rightState);
                        queue.add(rightState);
                    }
                }
            }

            System.out.println(ans);
        }
    }

    private static class State {
        int index;
        int leftSum;
        int rightSum;

        private State(int index, int leftSum, int rightSum) {
            this.index = index;
            this.leftSum = leftSum;
            this.rightSum = rightSum;
        }

        @Override
        public boolean equals(Object obj) {
            if (this == obj) return true;
            if (obj == null || obj.getClass() != this.getClass()) return false;

            State other = (State) obj;
            return this.index == other.index
                && this.leftSum == other.leftSum
                && this.rightSum == other.rightSum;
        }

        @Override
        public int hashCode() {
            int hashCode = this.index;
            hashCode = 31 * hashCode + this.leftSum;
            hashCode = 31 * hashCode + this.rightSum;

            return hashCode;
        }

        @Override
        public String toString() {
            return "State(" + this.index + ", " + this.leftSum + ", " + this.rightSum + ");";
        }
    }
}
