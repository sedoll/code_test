import java.io.*;
import java.util.*;

// 클래스 선언은 그대로 사용해도 좋습니다.
class Numbers {
    int index;
    int value;

    Numbers(int index, int value) {
        this.index = index;
        this.value = value;
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int T = Integer.parseInt(br.readLine()); // 테스트 케이스 개수

        for (int t=0; t<T; t++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int N = Integer.parseInt(st.nextToken()); // 문서의 개수
            int M = Integer.parseInt(st.nextToken()); // 궁금한 문서의 초기 위치

            // 1. 실제 문서들이 줄 서있는 큐
            LinkedList<Numbers> queue = new LinkedList<>();
            // 2. 중요도만 따로 저장해서 최댓값을 쉽게 확인하기 위한 우선순위 큐 (내림차순)
            PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());

            st = new StringTokenizer(br.readLine());
            for (int i = 0; i < N; i++) {
                int value = Integer.parseInt(st.nextToken());
                queue.add(new Numbers(i, value)); // (초기위치, 중요도)
                pq.add(value); // 중요도만 추가
            }

            int count = 0; // 몇 번째로 인쇄되는지

            while (!queue.isEmpty()) {
                Numbers current = queue.poll(); // 일단 맨 앞 문서를 꺼냄

                // 현재 꺼낸 문서의 중요도가, 남은 문서 중 가장 높은 중요도(pq.peek())와 같은가?
                if (!pq.isEmpty() && current.value == pq.peek()) {
                    // 인쇄 확정
                    pq.poll(); // 중요도 큐에서도 제거
                    count++;   // 인쇄 횟수 증가

                    // 우리가 찾던 그 문서(M)인가?
                    if (current.index == M) {
                        sb.append(count).append('\n');
                        break;
                    }
                } else {
                    // 중요도가 낮으면 다시 맨 뒤로 보냄
                    queue.add(current);
                }
            }
        }
        System.out.println(sb);
    }
}