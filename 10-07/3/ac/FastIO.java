import java.io.*;
import java.util.*;

public class FastIO {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        //Scanner scan = new Scanner(System.in);
        int T = Integer.parseInt(br.readLine());
        while (T-- > 0) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int m = Integer.parseInt(st.nextToken());
            int n = Integer.parseInt(st.nextToken());

            int[] ia = new int[m + 1];
            st = new StringTokenizer(br.readLine());
            for (int i = 0; i <= m; i++) {
                ia[i] = Integer.parseInt(st.nextToken());
            }
            int nnz = ia[m];
            int[] a = new int[nnz];
            int[] ja = new int[nnz];
            st = new StringTokenizer(br.readLine());
            for (int i = 0; i < nnz; i++) {
                a[i] = Integer.parseInt(st.nextToken());
            }
            st = new StringTokenizer(br.readLine());
            for (int i = 0; i < nnz; i++) {
                ja[i] = Integer.parseInt(st.nextToken());
            }


            StringBuilder sb = new StringBuilder();
            int a_ptr = 0;
            for (int row = 0; row < m; row++) {
                int[] matrix = new int[n];
                int in_row = ia[row + 1] - ia[row];
                for (int k = 0; k < in_row; k++) {
                    matrix[ja[a_ptr]] = a[a_ptr];
                    a_ptr++;
                }

                sb.append(matrix[0]);
                for (int i = 1; i < n; i++) {
                    sb.append(" ");
                    sb.append(matrix[i]);
                }
                sb.append("\n");
            }
            System.out.print(sb.toString());
        }
    }
}
