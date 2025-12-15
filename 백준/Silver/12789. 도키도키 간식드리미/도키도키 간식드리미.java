import java.io.*;
import java.util.*;
import java.util.stream.Collectors;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int max = Integer.parseInt(br.readLine());
        List<Integer> list = Arrays.stream(br.readLine().split(" "))
                .map(Integer::parseInt)
                .collect(Collectors.toList());
        Stack<Integer> stack = new Stack<>();

        boolean result = true;
        int ck = 1;
        for (int i=0; i<max; i++) {
            int num = list.remove(0);
            if (num == ck) {
                ck++;
                while (!stack.isEmpty() && stack.peek() == ck) {
                    ck++;
                    stack.pop();
                }
            } else {
                stack.push(num);
            }
        }

        if (stack.size() > 0) {
            result = false;
        }

        if (result) {
            System.out.println("Nice");
        } else {
            System.out.println("Sad");
        }
    }
}