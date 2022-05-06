package com.solve.algorithm.java.softeer;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class softeer633_비밀메뉴2 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		int K = Integer.parseInt(st.nextToken());
		String strShort = "";
		String strLong = "";
		if (N > M) {
			strLong = br.readLine().replace(" ", "");
			strShort = br.readLine().replace(" ", "");
		} else {
			strShort = br.readLine().replace(" ", "");
			strLong = br.readLine().replace(" ", "");
		}
		int size = strShort.length();
		int answer = 0;
		outer: while (size > 0) {
			for (int i = 0; i <= strShort.length() - size; i++) {
				String temp = strShort.substring(i, i + size);
				if (strLong.contains(temp)) {
					answer = size;
					break outer;
				}
			}
			size--;
		}
		System.out.println(answer);
	}
}
