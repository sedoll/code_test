import java.io.*;
import java.util.*;

public class Main{
    static int[][][] dp = new int[21][21][21];

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        StringTokenizer st = null;

        while(true) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());
            if(a == -1 && b == -1 && c == -1) {
                break;
            }
            sb.append("w(" + a + ", " + b + ", " + c + ") = " + fn(a, b, c)).append("\n");
        }
        System.out.println(sb);
    }

    static int fn(int a, int b, int c) {
        if ( a<= 0 || b<= 0 || c<= 0) {
            return 1;
        } else if (a > 20 || b > 20 || c > 20) {
            return fn(20, 20, 20);
        } else if (dp[a][b][c] != 0) {
            return dp[a][b][c];
        } else if (a < b && b < c) {
            dp[a][b][c] = fn(a, b, c-1) + fn(a, b-1, c-1) - fn(a, b-1, c);
        } else {
            dp[a][b][c] = fn(a-1, b, c) + fn(a-1, b-1, c) + fn(a-1, b, c-1) - fn(a-1, b-1, c-1);
        }
        return dp[a][b][c];
    }
}