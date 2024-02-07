class Solution {
    public String solution(int n) {
        String answer = "";
        int a = n/2;
        int b = n%2;
        if(n == 1) answer = "수";
        else if(n==2) answer = "수박";
        else {
            for(int i=0; i<a; i++) {
                answer += "수박";
            }
            if(b == 1) answer +="수";
        }

        return answer;
    }
}