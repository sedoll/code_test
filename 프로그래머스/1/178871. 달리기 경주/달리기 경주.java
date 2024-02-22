import java.util.*;

class Solution {
    public String[] solution(String[] players, String[] callings) {
        String[] answer = {};
        Map<String, Integer> map = new HashMap<>();
        for (int i = 0; i < players.length; i++) {
            map.put(players[i], i);
        }
        // System.out.println(map.toString());
        for(String call : callings) {
            int idx = map.get(call);
            // System.out.println(idx);
            
            map.put(players[idx-1], idx);
            map.put(players[idx], idx-1);
            
            String tmp = players[idx-1];
            players[idx-1] = players[idx];
            players[idx] = tmp;
            // System.out.println(map.toString());
        }
        answer = players;
        return answer;
    }
}