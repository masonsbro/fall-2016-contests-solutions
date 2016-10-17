import java.io.*;
import java.util.*;

public class Solution {
    private static void add(Map<String, Integer> freqMap, String gadget) {
        freqMap.put(gadget, freqMap.getOrDefault(gadget, 0) + 1);
    }

    private static void remove(Map<String, Integer> freqMap, String gadget) {
        freqMap.put(gadget, freqMap.getOrDefault(gadget, 0) - 1);
        if (freqMap.get(gadget) == 0) {
            freqMap.remove(gadget);
        }
    }

    private static int solve(String[] gadgets, int K) {
        // [start, end)
        int start = 0;
        int end = 0;

        int ans = gadgets.length;

        Map<String, Integer> freqMap = new HashMap<>();
        while (start < gadgets.length && !(freqMap.size() < K && end == gadgets.length)) {
            if (freqMap.size() < K) {
                add(freqMap, gadgets[end]);
                end++;
            } else {
                ans = Math.min(ans, end - start);
                remove(freqMap, gadgets[start]);
                start++;
            }
        }

        return ans;
    }

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int T = scan.nextInt();
        while (T-- > 0) {
            Set<String> allGadgets = new HashSet<>();
            int N = scan.nextInt();
            int K = scan.nextInt();
            String[] gadgets = new String[N];

            for (int i = 0; i < N; ++i) {
                gadgets[i] = scan.next();
                allGadgets.add(gadgets[i]);
            }

            if (K == 1) {
                System.out.println(1);
            } else if (allGadgets.size() < K) {
                System.out.println(-1);
            } else {
                System.out.println(solve(gadgets, K));
            }
        }
    }
}
