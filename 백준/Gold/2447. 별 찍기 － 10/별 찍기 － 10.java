import java.io.*;
import java.util.*;

public class Main{
    static char[][] chars;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        chars = new char[n][n];
        for (int i=0; i<n; i++) {
            for (int j=0; j<n; j++) {
                chars[i][j] = '*';
            }
        }
        fun(0, 0, n);
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                sb.append(chars[i][j]);
            }
            sb.append('\n'); // 줄바꿈
        }
        System.out.println(sb);
    }

    static void fun(int x, int y, int size) {
        if (size == 1) {
            return;
        }

        // 가운데 구멍
        int newSize = size / 3;
        for (int i = newSize+x; i<x+2*newSize; i++) {
            for (int j = newSize+y; j<y+2*newSize; j++) {
                chars[i][j] = ' ';
            }
        }

        // 재귀호출로 나머지 구멍내기
        for (int i=0; i<3; i++) {
            for (int j=0; j<3; j++) {
                if (i==1 && j==1) {
                    continue;
                }
                fun(newSize*i+x, newSize*j+y, newSize);
            }
        }
    }
}