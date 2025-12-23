import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        Deque<Integer> deque = new ArrayDeque<>();
        int[] arr = new int[100000];
        StringTokenizer st = null;
        StringBuilder sb = new StringBuilder();

        int n = Integer.parseInt(br.readLine());
        for (int i=0; i<2; i++) {
            st = new StringTokenizer(br.readLine());
            if (i==0) {
                for (int j=0; j<n; j++) {
                    int num = Integer.parseInt(st.nextToken());
                    arr[j] = num;
                }
            } else {
                for (int j=0; j<n; j++) {
                    int num = Integer.parseInt(st.nextToken());
                    if (arr[j] == 0) {
                        deque.add(num);
                    }
                }
            }
        }
        int m = Integer.parseInt(br.readLine());
        st = new StringTokenizer(br.readLine());
        for (int i=0; i<m; i++) {
            deque.addFirst(Integer.parseInt(st.nextToken()));
            sb.append(deque.removeLast()).append(" ");
        }
        System.out.println(sb);
    }
}