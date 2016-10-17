import java.io.*;
import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int T = scan.nextInt();
        while (T-- > 0) {
            int m = scan.nextInt();
            int n = scan.nextInt();
            scan.nextLine();

            int[] ia = new int[m + 1];
            for (int i = 0; i <= m; i++) {
                ia[i] = scan.nextInt();
            }
            int nnz = ia[m];
            int[] a = new int[nnz];
            int[] ja = new int[nnz];
            for (int i = 0; i < nnz; i++) {
                a[i] = scan.nextInt();
            }
            for (int i = 0; i < nnz; i++) {
                ja[i] = scan.nextInt();
            }

            int a_ptr = 0;
            for (int row = 0; row < m; row++) {
                int[] matrix = new int[n];
                int in_row = ia[row + 1] - ia[row];
                for (int k = 0; k < in_row; k++) {
                    matrix[ja[a_ptr]] = a[a_ptr];
                    a_ptr++;
                }

                System.out.print(matrix[0]);
                for (int i = 1; i < n; i++) {
                    System.out.print(" " + matrix[i]);
                }
                System.out.println();
            }
        }
    }
}
