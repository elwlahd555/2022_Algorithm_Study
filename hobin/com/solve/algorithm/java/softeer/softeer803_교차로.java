package com.solve.algorithm.java.softeer;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.StringTokenizer;

public class softeer803_교차로 {
	private static class Point {
		int number, time;

		public Point(int number, int time) {
			super();
			this.number = number;
			this.time = time;
		}
	}

	private static ArrayList<LinkedList<Point>> que;

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = null;
		int N = Integer.parseInt(br.readLine());
		que = new ArrayList<>();
		for (int i = 0; i < 4; i++) {
			que.add(new LinkedList<Point>());
		}
		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			int time = Integer.parseInt(st.nextToken());
			int location = st.nextToken().charAt(0) - 'A';
			que.get(location).add(new Point(i, time));
		}
		int cnt = 0;
		int answer[] = new int[N];
		Point A = null;
		Point B = null;
		Point C = null;
		Point D = null;
		while (check()) {
			A = null;
			B = null;
			C = null;
			D = null;
			for (int i = 0; i < que.size(); i++) {
				if (que.get(i).isEmpty()) {
					continue;
				}
				if (que.get(i).get(0).time <= cnt) {
					if (i == 0) {
						A = que.get(i).poll();
					} else if (i == 1) {
						B = que.get(i).poll();
					} else if (i == 2) {
						C = que.get(i).poll();
					} else {
						D = que.get(i).poll();
					}
				}
			}
			if (A != null && B != null && C != null && D != null) {
				answer[A.number] = -1;
				answer[B.number] = -1;
				answer[C.number] = -1;
				answer[D.number] = -1;
			}else if(A == null && B == null && C == null && D == null) {
				cnt++;
				continue;
			}else {
				if (A != null) {
					if (D == null) {
						answer[A.number] = cnt;
					} else {
						que.get(0).addFirst(A);
					}
				}
				if (B != null) {
					if (A == null) {
						answer[B.number] = cnt;
					} else {
						que.get(1).addFirst(B);
					}
				}
				if (C != null) {
					if (B == null) {
						answer[C.number] = cnt;
					} else {
						que.get(2).addFirst(C);
					}
				}
				if (D != null) {
					if (C == null) {
						answer[D.number] = cnt;
					} else {
						que.get(3).addFirst(D);
					}
				}
			}
			cnt++;
		}
		for (int i = 0; i < N; i++) {
			System.out.println(answer[i]);
		}
	}

	private static boolean check() {
		for (int i = 0; i < que.size(); i++) {
			if (!que.get(i).isEmpty()) {
				return true;
			}
		}
		return false;
	}
}
