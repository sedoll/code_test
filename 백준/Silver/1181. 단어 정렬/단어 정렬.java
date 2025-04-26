import java.io.*;
import java.lang.reflect.Array;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        Set<String> set = new HashSet<>();

        int value = Integer.parseInt(bf.readLine());
        for (int i = 0; i < value; i++) {
            set.add(bf.readLine());
        }
        List<String> list = new ArrayList<>(set);
        Collections.sort(list, Comparator.comparingInt(String::length).thenComparing(Comparator.naturalOrder()));
        for (String s : list) {
            bw.write(s+"\n");
        }
        bw.flush();
        bw.close();
    }
}
