import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    static class Medal {
        private int cty;
        private int gold;
        private int siv;
        private int brz;
        private int rank;

        Medal(int cty, int gold, int siv, int brz) {
            this.cty = cty;
            this.gold = gold;
            this.siv = siv;
            this.brz = brz;
        }

        public int getCty() {
            return cty;
        }

        public void setCty(int cty) {
            this.cty = cty;
        }

        public int getGold() {
            return gold;
        }

        public void setGold(int gold) {
            this.gold = gold;
        }

        public int getSiv() {
            return siv;
        }

        public void setSiv(int siv) {
            this.siv = siv;
        }

        public int getBrz() {
            return brz;
        }

        public void setBrz(int brz) {
            this.brz = brz;
        }

        public int getRank() {
            return rank;
        }

        public void setRank(int rank) {
            this.rank = rank;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        StringBuilder sb = new StringBuilder();
        List<Medal> list = new ArrayList<>();
        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());
        int result = 0;
        for (int i=0; i<N; i++) {
            st = new StringTokenizer(br.readLine());
            int c = Integer.parseInt(st.nextToken());
            int g = Integer.parseInt(st.nextToken());
            int s = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            list.add(new Medal(c, g, s, b));
        }
        list.sort(Comparator.comparingInt(Medal::getGold).reversed()
                .thenComparing(Comparator.comparingInt(Medal::getSiv).reversed())
                .thenComparing(Comparator.comparingInt(Medal::getBrz).reversed()));

        list.get(0).setRank(1);
        if (list.get(0).getCty() == K) {
            System.out.println(1);
            return;
        }
        int sum = 1;
        for (int i=1; i<list.size(); i++) {
            Medal m1 = list.get(i-1);
            Medal m2 = list.get(i);
            if (m1.getGold() == m2.getGold() &&
                    m1.getSiv() == m2.getSiv() &&
                    m1.getBrz() == m2.getBrz()) {
                m2.setRank(m1.getRank());
                sum++;
            } else {
                m2.setRank(m1.getRank()+sum);
                sum = 1;
            }
            if (m2.getCty() == K) {
                result = m2.getRank();
                break;
            }
        }
        System.out.println(result);
    }


}