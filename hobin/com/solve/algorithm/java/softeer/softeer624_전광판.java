package com.solve.algorithm.java.softeer;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class softeer624_전광판 {
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = null;
		boolean board[][] = { { true, true, true, false, true, true, true },
				{ false, false, true, false, false, true, false }, { true, false, true, true, true, false, true },
				{ true, false, true, true, false, true, true }, { false, true, true, true, false, true, false },
				{ true, true, false, true, false, true, true }, { true, true, false, true, true, true, true },
				{ true, true, true, false, false, true, false }, { true, true, true, true, true, true, true },
				{ true, true, true, true, false, true, true } };
		int T = Integer.parseInt(br.readLine());
		for (int t = 0; t < T; t++) {
			st = new StringTokenizer(br.readLine());
			String A = st.nextToken();
			String B = st.nextToken();
			int answer = 0;
			if (A.length() > B.length()) {
				for (int i = 0; i < A.length() - B.length(); i++) {
					for (int j = 0; j < board[0].length; j++) {
						if (board[A.charAt(i) - '0'][j]) {
							answer++;
						}
					}
				}
				for (int i = 0; i < B.length(); i++) {
					for (int j = 0; j < board[0].length; j++) {
						if ((!board[A.charAt(A.length() - B.length() + i) - '0'][j] && board[B.charAt(i) - '0'][j])
								|| (board[A.charAt(A.length() - B.length() + i) - '0'][j]
										&& !board[B.charAt(i) - '0'][j])) {
							answer++;
						}
					}
				}
			} else if (A.length() < B.length()) {
				for (int i = 0; i < B.length() - A.length(); i++) {
					for (int j = 0; j < board[0].length; j++) {
						if (board[B.charAt(i) - '0'][j]) {
							answer++;
						}
					}
				}
				for (int i = 0; i < A.length(); i++) {
					for (int j = 0; j < board[0].length; j++) {
						if ((!board[A.charAt(i) - '0'][j] && board[B.charAt(B.length() - A.length() + i) - '0'][j])
								|| (board[A.charAt(i) - '0'][j]
										&& !board[B.charAt(B.length() - A.length() + i) - '0'][j])) {
							answer++;
						}
					}
				}
			} else {
				for (int i = 0; i < B.length(); i++) {
					for (int j = 0; j < board[0].length; j++) {
						if ((!board[A.charAt(i) - '0'][j] && board[B.charAt(i) - '0'][j])
								|| (board[A.charAt(i) - '0'][j] && !board[B.charAt(i) - '0'][j])) {
							answer++;
						}
					}
				}
			}
			System.out.println(answer);
		}
	}
}
