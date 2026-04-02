import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        
        // 문제 조건: 9*M/10을 올림한 값 이상이어야 함
        int target = (int) Math.ceil((9.0 * M) / 10.0);
        
        int[] inputArr = new int[N];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            inputArr[i] = Integer.parseInt(st.nextToken());
        }

        // 각 숫자의 빈도수를 저장할 배열 (값의 범위는 1,000,000까지)
        int[] count = new int[1000001];
        boolean found = false;

        // 1. 처음 M일간의 윈도우 구성
        for (int i = 0; i < M; i++) {
            int val = inputArr[i];
            count[val]++;
            if (count[val] >= target) {
                found = true;
                break;
            }
        }

        // 2. 윈도우를 한 칸씩 이동 (슬라이딩 윈도우)
        if (!found) {
            for (int i = M; i < N; i++) {
                // 나가는 원소(i-M번째) 처리
                int out = inputArr[i - M];
                count[out]--;

                // 들어오는 원소(i번째) 처리
                int in = inputArr[i];
                count[in]++;

                if (count[in] >= target) {
                    found = true;
                    break;
                }
            }
        }

        System.out.println(found ? "YES" : "NO");
    }
}