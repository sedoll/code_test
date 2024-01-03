import java.util.Scanner;

public class App {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        sc.nextLine();
        String b = sc.nextLine();
        char[] arr = b.toCharArray();
        int res = 0;
        for(int i=0; i<arr.length; i++) {
            res += Character.getNumericValue(arr[i]);
        }
        System.out.println(res);
    }
}
