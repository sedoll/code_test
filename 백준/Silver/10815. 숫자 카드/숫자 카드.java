import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        int[] cards = new int[N];
        String num1 = br.readLine();
        String[] tokens = num1.split("\\s+"); // 공백 기준 분리
        for (int i = 0; i < N; i++) {
            cards[i] = Integer.parseInt(tokens[i]);
        }
        Arrays.sort(cards);

        int M = Integer.parseInt(br.readLine());
        int[] queries = new int[M];
        String num2 = br.readLine();
        String[] tokens2 = num2.split("\\s+"); // 공백 기준 분리
        for (int i = 0; i < M; i++) {
            queries[i] = Integer.parseInt(tokens2[i]);
        }

        StringBuilder sb = new StringBuilder();
        for (int query : queries) {
            if (Arrays.binarySearch(cards, query) >= 0) {
                sb.append("1 ");
            } else {
                sb.append("0 ");

            }
        }
        System.out.println(sb);
    }
}