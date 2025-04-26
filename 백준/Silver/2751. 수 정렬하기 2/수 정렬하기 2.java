import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int idx = Integer.parseInt(bf.readLine());
        List<Integer> list = new ArrayList<>();
        for (int i = 0; i < idx; i++) {
            String str = bf.readLine();
            list.add(Integer.parseInt(str));
        }
        Collections.sort(list);
        for (Integer value : list) {
            bw.write(value +"\n");
        }
        bw.flush();
        bw.close();
    }
}
