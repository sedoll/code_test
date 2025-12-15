import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        Deque<Integer> deque = new ArrayDeque<>();

        int n = Integer.parseInt(br.readLine());
        for(int i=1; i<=n; i++) {
            deque.add(i);
        }

        while(true) {
            if (deque.size() == 1) break;
            deque.removeFirst(); // 없앤다.
            if (deque.size() == 1) break;
            deque.add(deque.removeFirst()); // 맨 첫번째 값을 맨 뒤에 넣는다.
        }
        System.out.println(deque.pop());
    }
}