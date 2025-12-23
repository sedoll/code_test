import java.io.*;
import java.util.*;

class Words {
    String word;
    int count;
    int length;

    public Words(String word, int count, int length) {
        this.word = word;
        this.count = count;
        this.length = length;
    }

}

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        Map<String, Integer> map = new HashMap<>();
        StringTokenizer st = null;
        StringBuilder sb = new StringBuilder();
        st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        for (int i = 0; i < n; i++) {
            String word = br.readLine();
            if (word.length() >= m && map.get(word) == null) {
                map.put(word, 1);
            } else if (word.length() >= m && map.get(word) != null) {
                map.put(word, map.get(word) + 1);
            }
        }
        List<Words> words = new ArrayList<>();

        for (Map.Entry<String, Integer> entry : map.entrySet()) {
            words.add(new Words(entry.getKey(), entry.getValue(), entry.getKey().length()));
        }

        Collections.sort(words, (w1, w2) -> {
            if (w1.count != w2.count) return w2.count - w1.count;
            if (w1.length != w2.length) return w2.length - w1.length;
            return w1.word.compareTo(w2.word);
        });

        for (Words word : words) {
            sb.append(word.word).append("\n");
        }

        System.out.println(sb);
    }
}