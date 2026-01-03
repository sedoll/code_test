import java.io.*;
import java.util.*;

public class Main{
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String line;
        StringBuilder sb = new StringBuilder();
        while ((line = br.readLine()) != null && !line.isEmpty()) {
            int input = Integer.parseInt(line);
            String n3 = "- -   - -         - -   - -";
            if (input == 0) {
                sb.append("-\n");
            } else if (input == 1) {
                sb.append("- -\n");
            } else if (input == 2) {
                sb.append("- -   - -\n");
            } else if (input == 3) {
                sb.append(n3+"\n");
            } else if (input > 3) {
                sb.append(fun(n3, 3, input)).append("\n");
            }
        }
        System.out.println(sb);
    }

    static String fun(String s, int start, int max) {
        if (start == max) {
            return s;
        } else {
            int pow = (int) Math.pow(3, start);
            String temp = s;
            String s1 = " ".repeat(pow);
            s += s1;
            s+= temp;
            return fun(s, start+1, max);
        }
    }
}