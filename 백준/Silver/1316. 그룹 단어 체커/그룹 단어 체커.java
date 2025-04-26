import java.io.*;
import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int idx = Integer.parseInt(bf.readLine());
        int res = 0;
        for (int i=0; i<idx; i++) {
            String str = bf.readLine();
            char[] chars = str.toCharArray();
            List<Character> ckList = new ArrayList<>();
            if (chars.length <= 2) {
                res += 1;
            } else {
                boolean ck = true;
                try {
                    for (int j=0; j<=chars.length-1; j++) {
                        if (j == chars.length-1 && !ckList.contains(chars[j])) {
                            ckList.add(chars[j]);
                        } else if (chars[j] == chars[j+1]) {
                            continue;
                        } else if (chars[j] != chars[j+1] && !ckList.contains(chars[j])) {
                            ckList.add(chars[j]);
                        } else if (j == chars.length-1 && !ckList.contains(chars[j])) {
                            ckList.add(chars[j]);
                        } else {
                            ck = false;
                            break;
                        }
                    }
                } catch (Exception e) {
                    ck = false;
                }
                if (ck) {
                    res += 1;
                }
            }
        }
        bw.write(String.valueOf(res));
        bw.flush();
        bw.close();
    }
}