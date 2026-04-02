import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        boolean[] booleans = new boolean[1000001];
        int cnt = 0;
        int n = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        int x = Integer.parseInt(br.readLine());
        for (int i=0; i<n; i++) {
            int v = Integer.parseInt(st.nextToken());
            int target = x - v;
            if (target >= 1 && target <= 1000000 && booleans[target]) {
                cnt++;
            } else {
                booleans[v] = true;
            }
        }
        System.out.println(cnt);
    }
}