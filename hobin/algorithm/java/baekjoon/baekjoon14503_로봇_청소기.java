package algorithm.java.baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class baekjoon14503_로봇_청소기 {
	private static class Point {
		int x, y, direct;

		public Point(int x, int y, int direct) {
			super();
			this.x = x;
			this.y = y;
			this.direct = direct;
		}

	}

	private static int dx[] = { -1, 0, 1, 0 };
	private static int dy[] = { 0, 1, 0, -1 };
	private static int map[][];
	private static boolean visited[][];
	private static int N, M;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		st = new StringTokenizer(br.readLine());
		Point robot = new Point(Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken()),
				Integer.parseInt(st.nextToken()));
		map = new int[N][M];
		visited = new boolean[N][M];
		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < M; j++) {
				map[i][j] = Integer.parseInt(st.nextToken());
				if (map[i][j] == 1) {
					visited[i][j] = true;
				}
			}
		}
		int answer = 0;
		outer: while (check()) {
			if (!visited[robot.x][robot.y]) {
				visited[robot.x][robot.y] = true;
				answer++;
			}
			int k = 0;
			while (k < 4) {
				robot.direct--;
				if (robot.direct < 0) {
					robot.direct = 3;
				}
				int x = robot.x + dx[robot.direct];
				int y = robot.y + dy[robot.direct];
				if (!visited[x][y]) {
					robot.x = x;
					robot.y = y;
					break;
				}
				k++;
				if (k == 4) {
					if (map[robot.x - dx[robot.direct]][robot.y - dy[robot.direct]] == 1) {
						break outer;
					} else {
						robot.x = robot.x - dx[robot.direct];
						robot.y = robot.y - dy[robot.direct];
						break;
					}
				}
			}
		}
		System.out.println(answer);
	}

	private static boolean check() {
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				if (!visited[i][j]) {
					return true;
				}
			}
		}
		return false;
	}
}
