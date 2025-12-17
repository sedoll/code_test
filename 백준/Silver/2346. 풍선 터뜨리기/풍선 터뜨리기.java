import java.io.*;
import java.util.*;

class Balloon {
    int index;
    int value;
    Balloon(int index, int value) {
        this.index = index;
        this.value = value;
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        Deque<Balloon> deque = new ArrayDeque<>();
        StringBuilder sb = new StringBuilder();
        int n = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i=1; i<=n; i++) {
            deque.add( new Balloon(i,Integer.parseInt(st.nextToken())));
        }
        int cnt = 1;
        Balloon balloon = null;
        while(deque.size()>0) {
            if (cnt == 1) {
                balloon = deque.removeFirst();
                sb.append(balloon.index).append(" ");
                cnt++;
            }
            if (balloon.value > 0) { // 오른쪽 이동
                for (int i=0; i<balloon.value-1; i++) {
                    deque.addLast(deque.removeFirst());
                }
                balloon = deque.removeFirst();
            } else if (balloon.value < 0) { // 왼쪽 이동
                for (int i=balloon.value; i<0; i++) {
                    deque.addFirst(deque.removeLast());
                }
                balloon = deque.removeFirst();
            }
            sb.append(balloon.index).append(" ");
        }
        System.out.println(sb);
    }
}