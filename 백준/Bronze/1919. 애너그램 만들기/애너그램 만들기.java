import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        String s1 = br.readLine();
        char[] chars1 = s1.toCharArray();
        int[] arr1 = new int[26];
        String s2 = br.readLine();
        char[] chars2 = s2.toCharArray();
        int[] arr2 = new int[26];
        int res = 0;
        for (int i=0; i<chars1.length; i++) {
            sb.append(chars1[i]).append("\n");
            arr1[chars1[i]-'a']++;
        }
        for (int i=0; i<chars2.length; i++) {
            sb.append(chars2[i]).append("\n");
            arr2[chars2[i]-'a']++;
        }
        for (int i=0; i<26; i++) {
            res += Math.abs(arr1[i] - arr2[i]);
        }
        System.out.println(res);
    }
}