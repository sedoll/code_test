import java.io.*;
import java.util.*;
import java.math.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int N = Integer.parseInt(br.readLine());
        for (int i=0; i<N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int r = Integer.parseInt(st.nextToken());
            int n = Integer.parseInt(st.nextToken());
            r = Math.min(r, n-r);
            BigInteger bi = BigInteger.ONE;
            for (int j=0; j<r; j++) {
                bi = bi.multiply(BigInteger.valueOf(n-j));
                bi = bi.divide(BigInteger.valueOf(j+1));
            }
            sb.append(bi).append(" ");
        }
        System.out.println(sb);
    }
}