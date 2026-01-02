import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        StringTokenizer st = null;
        List<Integer> list = new ArrayList<>();
        st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());
        for (int i=1; i<=N; i++) {
            list.add(i);
        }
        while(!list.isEmpty()) {
            for (int i = 0; i < k-1; i++) {
                list.add(list.remove(0));
            }
            if (list.size() == 1) {
                sb.append(list.remove(0));
            } else {
                sb.append(list.remove(0)).append(", ");
            }
        }
        System.out.println("<" + sb + ">");
    }
}