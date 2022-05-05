package com.sovle.algorithm.java.baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class baekjoon23291_어항_정리 {
	private static int N, K;
	private static int fish[][];
	private static int dx[] = { -1, 1, 0, 0 };
	private static int dy[] = { 0, 0, -1, 1 };

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		K = Integer.parseInt(st.nextToken());
		fish = new int[N][25];
		st = new StringTokenizer(br.readLine());
		for (int i = 0; i < N; i++) {
			fish[i][0] = Integer.parseInt(st.nextToken());
		}
		int answer = 0;
		while (check()) {
			addFish();
			firstFold();
			fishMove();
			spread();
			secondFold();
			fishMove();
			spread();
			answer++;
		}
		System.out.println(answer);
	}

	private static boolean check() {
		int max = 0;
		int min = Integer.MAX_VALUE;
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < fish[0].length; j++) {
				if (fish[i][j] > 0) {
					max = Math.max(fish[i][j], max);
					min = Math.min(fish[i][j], min);
				}
			}
		}
		if (max - min <= K) {
			return false;
		} else {
			return true;
		}
	}

	private static void secondFold() {
		for (int i = 0; i < N / 2; i++) {
			fish[N - 1 - i][1] = fish[i][0];
			fish[i][0] = 0;
		}
		for (int i = 0; i < N / 4; i++) {
			for (int j = 0; j < 2; j++) {
				fish[N - 1 - i][3 - j] = fish[N / 2 + i][j];
				fish[N / 2 + i][j] = 0;
			}
		}
	}

	private static void spread() {
		int temp[] = new int[N];
		int k = 0;
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < fish[0].length; j++) {
				if (fish[i][j] > 0) {
					temp[k] = fish[i][j];
					fish[i][j] = 0;
					k++;
				}
			}
		}
		for (int i = 0; i < N; i++) {
			fish[i][0] = temp[i];
		}
	}

	private static void fishMove() {
		int tempFish[][] = new int[N][25];
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < 25; j++) {
				if (fish[i][j] == 0) {
					break;
				}
				for (int k = 0; k < 4; k++) {
					int x = i + dx[k];
					int y = j + dy[k];
					if (x < 0 || x >= N || y < 0 || y >= 25 || fish[x][y] == 0 || fish[i][j] < fish[x][y]) {
						continue;
					}
					tempFish[x][y] += (fish[i][j] - fish[x][y]) / 5;
					tempFish[i][j] -= (fish[i][j] - fish[x][y]) / 5;
				}
			}
		}
		for (int i = 0; i < tempFish.length; i++) {
			for (int j = 0; j < tempFish[0].length; j++) {
				fish[i][j] += tempFish[i][j];
			}
		}
	}

	private static void addFish() {
		int min = Integer.MAX_VALUE;
		for (int i = 0; i < N; i++) {
			if (fish[i][0] < min) {
				min = fish[i][0];
			}
		}
		for (int i = 0; i < N; i++) {
			if (fish[i][0] == min) {
				fish[i][0]++;
			}
		}
	}

	private static void firstFold() {
		int startX = 0;
		int vert = 1;
		int hori = 1;
		while (startX + vert + hori <= N) {
			for (int i = vert - 1; i >= 0; i--) {
				for (int j = 0; j < hori; j++) {
					int nx = startX + vert + j;
					int ny = vert - i;
					fish[nx][ny] = fish[startX + i][j];
					fish[startX + i][j] = 0;
				}
			}
			startX += vert;
			if (vert == hori)
				hori++;
			else
				vert++;
		}
	}
}
