import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        List<Long> list = new ArrayList<>();
        // 첫 줄 처리
        String firstLine = br.readLine();
        String[] firstTokens = firstLine.split("\\s+");

        int N = Integer.parseInt(firstTokens[0]); // 첫 번째 값은 N

        // 첫 줄 안의 나머지 숫자들은 데이터
        for (int i = 1; i < firstTokens.length; i++) {
            String reversed = new StringBuilder(firstTokens[i]).reverse().toString();
            list.add(Long.parseLong(reversed));
        }

        while (list.size() < N) {
            String line = br.readLine();
            if (line == null || line.isEmpty()) continue;

            String[] tokens = line.split("\\s+"); // 공백 기준 분리
            for (String token : tokens) {
                String reverseToken = new StringBuilder(token).reverse().toString();
                long longValue = Long.parseLong(reverseToken);
                list.add(longValue);
                if (list.size() == N) break;
            }
        }
        Collections.sort(list);
        StringBuilder sb = new StringBuilder();
        for (Long value : list) {
            sb.append(value + "\n");
        }
        System.out.println(sb);
    }
}