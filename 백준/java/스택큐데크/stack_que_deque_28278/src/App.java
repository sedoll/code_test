import java.io.*;
import java.util.ArrayList;
import java.util.List;

public class App {
    public static void main(String[] args) throws IOException {
        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in)); // 버퍼 입력
        StringBuffer sb = new StringBuffer(); // 버퍼 출력내용 담기, String 타입
        
        int n = Integer.parseInt(br.readLine()); // 반복 횟수
        List<String> stack = new ArrayList<>(); // list 형 변수 생성

        for(int i=0; i<n; i++) {    // 실행
            String[] n2 = br.readLine().split(" "); // 두 개 이상이면 split으로 나눔
            String a = n2[0];

            if(a.equals("1")) { // 1번
                stack.add(n2[1]); // 스택에 추가
            } else if (a.equals("2")) { // 2번
                if(stack.size() == 0) { // 0 이면 -1
                    sb.append("-1\n");
                } else { // 1 이상이면 맨 위의 값 추출
                    sb.append(stack.get(stack.size()-1) + "\n");
                    stack.remove(stack.size()-1);
                }
            } else if (a.equals("3")) { // 3번
                sb.append(stack.size() + "\n"); // 사이즈 출력
            } else if (a.equals("4")) { // 4번
                sb.append(stack.size() == 0 ? "1\n" : "0\n"); // 스택 내부의 값이 없으면 1, 있으면 0
            } else if (a.equals("5")) { // 5번
                sb.append(stack.size() > 0 ? stack.get(stack.size()-1) + "\n" : "-1\n"); // 개수가 1 이상이면 맨 위의 값 출력, 없으면 -1
            } 
        }
        
        br.close(); // bufferedreader 닫기
        
        System.out.println(sb); // 저장된 출력 문자열 sout
    }
}