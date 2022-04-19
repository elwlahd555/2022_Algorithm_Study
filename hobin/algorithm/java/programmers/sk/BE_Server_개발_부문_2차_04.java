package algorithm.java.programmers.sk;

import java.util.LinkedList;

public class BE_Server_개발_부문_2차_04 {
	public static void main(String[] args) {
		int n=8;
		int m=4;
		int k=4;
		int records[][]= {{1, 5, 1, 3}, {5, 7, 5, 6}};
		System.out.println(solution(n, m, k, records));
	}
	private static LinkedList<String> list;
	private static int nMap[],mMap[];
    public static int[] solution(int n, int m, int k, int[][] records) {
        int[] answer = {};
        list=new LinkedList<>();
        nMap=new int[n+1];
        mMap=new int[k+1];
        for (int i = 0; i < records.length; i++) {
			for (int j = 0; j < records.length; j++) {
				nMap[records[i][j]]=1;
			}
			dfs(n,m,k,1,1);
		}
        return answer;
    }
	private static void dfs(int n, int m, int k, int cnt,int start) {
		if(cnt==k+1) {

			return;
		}
		for (int i = 0; i < n+1; i++) {
			if(nMap[i]==1) {
				for (int j = start; j <= m; j++) {
					if(cnt<=j) {
						mMap[cnt]=j;
						dfs(n,m,k,cnt+1,j+1);
					}
				}
			}
		}
	}
}
