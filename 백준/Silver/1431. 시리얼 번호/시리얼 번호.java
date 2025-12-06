import java.io.*;
import java.util.*;

class SerialSort {
    private String value;
    private int length;
    private int sum;
    SerialSort(String value, int length, int sum) {
        this.value = value;
        this.length = length;
        this.sum = sum;
    }
    public String getValue() {
        return value;
    }
    public int getLength() {
        return length;
    }
    public int getSum() {
        return sum;
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int cnt = Integer.parseInt(br.readLine());
        List<SerialSort> list = new ArrayList<>();
        for (int i = 0; i < cnt; i++) {
            String value = br.readLine();
            int sum = 0;
            int length = value.length();
            for (char c : value.toCharArray()) {
                if (Character.isDigit(c)) {
                    sum += c - '0';  // 숫자 변환
                }
            }
            list.add(new SerialSort(value, length, sum));
        }
        Collections.sort(list, Comparator.comparing(SerialSort::getLength)
                .thenComparing(SerialSort::getSum)
                .thenComparing(SerialSort::getValue));
        StringBuilder sb = new StringBuilder();
        for (SerialSort s : list) {
            sb.append(s.getValue() + "\n");
        }
        System.out.println(sb);
    }
}