import java.util.Scanner;

public class App {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        
        int a = Integer.parseInt(sc.nextLine());
        String b = sc.nextLine();
        String[] arr = b.split(" ");
        float res = 0f;
        float max = 0f;

        for(int i=0; i<arr.length; i++) {
            float f = Float.parseFloat(arr[i]);
            res += f;
            if(max < f) max = f;
        }
        res = res / a;
        System.out.println((res/max)*100);
    }
}