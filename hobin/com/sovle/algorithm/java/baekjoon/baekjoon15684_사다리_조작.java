package com.sovle.algorithm.java.baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class baekjoon15684_사다리_조작 {
	private static int N, M, H, answer;
	private static int[][] map;
	private static boolean finish;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		H = Integer.parseInt(st.nextToken());
		finish = false;
		map = new int[H + 1][N + 1];

		int x, y;
		for (int i = 0; i < M; i++) {
			st = new StringTokenizer(br.readLine());
			x = Integer.parseInt(st.nextToken());
			y = Integer.parseInt(st.nextToken());
			map[x][y] = 1;
			map[x][y + 1] = 2;
		}

		for (int i = 0; i <= 3; i++) {
			answer = i;
			dfs(1, 0);
			if (finish)
				break;
		}
		if (!finish) {
			answer = -1;
		}
		System.out.println(answer);
	}

	private static void dfs(int x, int cnt) {
		if (finish)
			return;
		if (answer == cnt) {
			if (check())
				finish = true;
			return;
		}
		for (int i = x; i < H + 1; i++) {
			for (int j = 1; j < N; j++) {
				if (map[i][j] == 0 && map[i][j + 1] == 0) {
					map[i][j] = 1;
					map[i][j + 1] = 2;
					dfs(i, cnt + 1);
					map[i][j] = map[i][j + 1] = 0;
				}
			}
		}
	}

	private static boolean check() {
		for (int i = 1; i <= N; i++) {
			int x = 1, y = i;
			for (int j = 0; j < H; j++) {
				if (map[x][y] == 1) {
					y++;
				} else if (map[x][y] == 2) {
					y--;
				}
				x++;
			}
			if (y != i)
				return false;
		}
		return true;
	}

}
