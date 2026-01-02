import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int N = Integer.parseInt(br.readLine());
        int[] arr = new int[N];
        int sum = 0;
        for (int i=0; i<N; i++) {
            arr[i] = Integer.parseInt(br.readLine());
            sum += arr[i];
        }
        Arrays.sort(arr);
        int avm = (int) Math.round(N * 0.15);
        for (int i=0; i<avm; i++) {
            sum -= arr[i];
        }
        for (int i=N-avm; i<N; i++) {
            sum -= arr[i];
        }
        System.out.println((int) Math.round((double) sum/(N-(2*avm))));
    }
}