import java.util.Scanner;

public class App {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        String s = sc.nextLine();
        int[] res = new int[26];

        for(int i=0; i<res.length; i++) {
            res[i] = s.indexOf((char) (97+i));
            System.out.println(res[i]);
        }
    }
}
