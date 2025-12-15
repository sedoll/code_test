import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        Deque<Integer> deque = new ArrayDeque<>();
        StringBuilder sb = new StringBuilder();
        int n = Integer.parseInt(br.readLine());
        for (int i=0; i<n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            String a = st.nextToken();
            int b = 0;
            if (a.equals("push")) {
                deque.add(Integer.parseInt(st.nextToken()));
            } else if (a.equals("pop")) {
                if (deque.isEmpty()) {
                    sb.append("-1").append("\n");
                } else {
                    sb.append(deque.removeFirst()).append("\n");
                }
            } else if (a.equals("size")) {
                sb.append(deque.size()).append("\n");
            } else if (a.equals("empty")) {
                sb.append(deque.isEmpty() == true ? 1 : 0).append("\n");
            } else if (a.equals("front")) {
                if (deque.isEmpty()) {
                    sb.append("-1").append("\n");
                } else {
                    sb.append(deque.getFirst()).append("\n");
                }
            } else if (a.equals("back")) {
                if (deque.isEmpty()) {
                    sb.append("-1").append("\n");
                } else {
                    sb.append(deque.getLast()).append("\n");
                }
            }
        }
        System.out.println(sb);
    }
}