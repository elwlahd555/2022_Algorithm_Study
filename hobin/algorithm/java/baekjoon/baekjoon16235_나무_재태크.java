package algorithm.java.baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Collections;
import java.util.LinkedList;
import java.util.StringTokenizer;

public class baekjoon16235_나무_재태크 {
	private static class tree implements Comparable<tree> {
		int x, y, age;

		public tree(int x, int y, int age) {
			super();
			this.x = x;
			this.y = y;
			this.age = age;
		}

		@Override
		public int compareTo(tree o) {
			return this.age - o.age;
		}
	}

	private static int dx[] = { -1, -1, -1, 0, 0, 1, 1, 1 };
	private static int dy[] = { -1, 0, 1, -1, 1, -1, 0, 1 };

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		int K = Integer.parseInt(st.nextToken());
		int orginalmap[][] = new int[N + 1][N + 1];
		int map[][] = new int[N + 1][N + 1];
		LinkedList<tree> treeList = new LinkedList<>();
		LinkedList<tree> deadTreeList = new LinkedList<>();
		for (int i = 1; i <= N; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 1; j <= N; j++) {
				int temp = Integer.parseInt(st.nextToken());
				map[i][j] = 5;
				orginalmap[i][j] = temp;
			}
		}
		for (int i = 0; i < M; i++) {
			st = new StringTokenizer(br.readLine());
			int x = Integer.parseInt(st.nextToken());
			int y = Integer.parseInt(st.nextToken());
			int z = Integer.parseInt(st.nextToken());
			treeList.add(new tree(x, y, z));
		}
		Collections.sort(treeList);
		while (K > 0) {
			if (treeList.isEmpty()) {
				break;
			}
			int size = treeList.size();
			// SPRING
			for (int i = 0; i < size; i++) {
				tree t = treeList.poll();
				if (map[t.x][t.y] >= t.age) {
					map[t.x][t.y] -= t.age;
					t.age++;
					treeList.add(t);
				} else {
					deadTreeList.add(t);
				}
			}
			// SUMMER
			size = deadTreeList.size();
			for (int i = 0; i < size; i++) {
				tree t = deadTreeList.poll();
				map[t.x][t.y] += t.age / 2;
			}
			// FALL
			size = treeList.size();
			for (int i = 0; i < size; i++) {
				tree t = treeList.poll();
				if (t.age % 5 == 0) {
					for (int k = 0; k < 8; k++) {
						int x = t.x + dx[k];
						int y = t.y + dy[k];
						if (x <= 0 || x > N || y <= 0 || y > N) {
							continue;
						}
						treeList.add(new tree(x, y, 1));
					}
				}
				treeList.add(t);
			}
			// WINTER
			for (int i = 0; i <= N; i++) {
				for (int j = 0; j <= N; j++) {
					map[i][j] += orginalmap[i][j];
				}
			}
			Collections.sort(treeList);
			K--;
		}
		System.out.println(treeList.size());
	}
}
