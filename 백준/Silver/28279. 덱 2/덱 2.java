import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        Deque<Integer> deque = new ArrayDeque<>();
        StringBuilder sb = new StringBuilder();
        int n = Integer.parseInt(br.readLine());
        for(int i=0; i<n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            if (a == 1) {
                int b = Integer.parseInt(st.nextToken());
                deque.addFirst(b);
            } else if (a == 2) {
                int b = Integer.parseInt(st.nextToken());
                deque.add(b);
            }else if (a == 3) {
                if (!deque.isEmpty()) {
                    sb.append(deque.removeFirst()).append("\n");
                } else {
                    sb.append(-1).append("\n");
                }
            } else if (a == 4) {
                if (!deque.isEmpty()) {
                    sb.append(deque.removeLast()).append("\n");
                } else {
                    sb.append(-1).append("\n");
                }
            } else if (a == 5) {
                sb.append(deque.size()).append("\n");
            } else if (a == 6) {
                if (!deque.isEmpty()) {
                    sb.append(0).append("\n");
                } else {
                    sb.append(1).append("\n");
                }
            } else if (a == 7) {
                if (!deque.isEmpty()) {
                    sb.append(deque.getFirst()).append("\n");
                } else {
                    sb.append(-1).append("\n");
                }
            } else {
                if (!deque.isEmpty()) {
                    sb.append(deque.getLast()).append("\n");
                } else {
                    sb.append(-1).append("\n");
                }
            }
        }
        System.out.println(sb);
    }
}