import java.io.*;
import java.util.*;

public class Main{
    public static List<Integer> recursion(String s, int l, int r){
        if(l >= r) {
            return new ArrayList<>(Arrays.asList(1, l+1));
        } else if (s.charAt(l) != s.charAt(r)) {
            return new ArrayList<>(Arrays.asList(0, l+1));
        }
        else return recursion(s, l+1, r-1);
    }
    public static List<Integer> isPalindrome(String s){
        return recursion(s, 0, s.length()-1);
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int N = Integer.parseInt(br.readLine());
        for (int i=0; i<N; i++) {
            List<Integer> list = new ArrayList<>();
            String s = br.readLine();
            list = isPalindrome(s);
            sb.append(list.get(0)+" "+list.get(1)+"\n");
        }
        System.out.println(sb);
    }
}