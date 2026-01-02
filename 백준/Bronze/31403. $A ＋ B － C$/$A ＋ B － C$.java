import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        String  a = br.readLine();
        String  b = br.readLine();
        int c = Integer.parseInt(br.readLine());
        int res1 = Integer.parseInt(a) + Integer.parseInt(b) - c;
        int res2 = Integer.parseInt(a+b)-c;
        System.out.println(res1);
        System.out.println(res2);
    }
}