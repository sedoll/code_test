import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        StringTokenizer st;
        int n = Integer.parseInt(br.readLine());
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            int x1 = Integer.parseInt(st.nextToken());
            int y1 = Integer.parseInt(st.nextToken());
            int r1 = Integer.parseInt(st.nextToken());
            int x2 = Integer.parseInt(st.nextToken());
            int y2 = Integer.parseInt(st.nextToken());
            int r2 = Integer.parseInt(st.nextToken());
            // 두 점 사이 거리의 제곱 (d^2)
            int dPow2 = (int)(Math.pow(x2 - x1, 2) + Math.pow(y2 - y1, 2));
            // 반지름 합의 제곱 (r1 + r2)^2
            int sumR = (int)Math.pow(r1 + r2, 2);
            // 반지름 차의 제곱 (r1 - r2)^2
            int diffR = (int)Math.pow(r1 - r2, 2);
            if (dPow2 == 0 && r1 == r2) {// 일치
                sb.append("-1\n");
            } else if (dPow2 > sumR) {// 외부에서 만나지 않음
                sb.append("0\n");
            } else if (dPow2 < diffR) {// 내부에서 만나지 않음
                sb.append("0\n");
            } else if (dPow2 == sumR) {// 외접
                sb.append("1\n");
            } else if (dPow2 == diffR) {// 내접
                sb.append("1\n");
            } else {// 두 점 교차
                sb.append("2\n");
            }
        }
        System.out.println(sb);
    }
}