import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int n = Integer.parseInt(br.readLine());
        
        // 1. 자료구조 타입 저장 (배열 크기를 n으로 동적 할당)
        int[] typeArr = new int[n]; 
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            typeArr[i] = Integer.parseInt(st.nextToken());
        }

        // 2. 초기값 처리 (큐인 경우만 덱에 추가)
        // 작성하신 대로 뒤로 넣고(add), 앞으로 넣어서(addFirst), 뒤로 빼는(removeLast) 로직 유지
        Deque<Integer> deque = new ArrayDeque<>();
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            int num = Integer.parseInt(st.nextToken());
            if (typeArr[i] == 0) {
                deque.addLast(num); // 명시적으로 addLast라고 쓰는 게 더 이해하기 쉬움
            }
        }

        // 3. 삽입 및 출력
        int m = Integer.parseInt(br.readLine());
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < m; i++) {
            int insertValue = Integer.parseInt(st.nextToken());
            deque.addFirst(insertValue); // 입구로 넣고
            sb.append(deque.pollLast()).append(" "); // 출구로 뺌 (pollLast가 removeLast보다 안전 - 비어있을 때 에러 안 남)
        }

        System.out.println(sb);
    }
}