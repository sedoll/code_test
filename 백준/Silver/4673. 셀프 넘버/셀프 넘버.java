import java.io.*;
import java.lang.reflect.Array;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        List<Integer> ckNum = new ArrayList<>();
        List<Integer> selfNum = new ArrayList<>();
        for (int i = 1; i <= 10000; i++) {
            String strNumber = String.valueOf(i);
            Integer sum = i;
            for (int j = 0; j < strNumber.length(); j++) {
                sum += strNumber.charAt(j) - '0';
            }
            if (!ckNum.contains(i)) {
                selfNum.add(i);
                ckNum.add(i);
            }
            if (!ckNum.contains(sum)) {
                ckNum.add(sum);
            }
        }

        for (Integer res : selfNum) {
            bw.write(res+"\n");
        }
        bw.flush();
        bw.close();
    }
}
