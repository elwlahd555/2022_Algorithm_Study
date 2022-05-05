package com.sovle.algorithm.java.baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class baekjoon13458_시험_감독 {
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
		int N=Integer.parseInt(br.readLine());
		int map[]=new int[N];
		long answer=0;
		StringTokenizer st=new StringTokenizer(br.readLine());
		for (int i = 0; i < N; i++) {
			map[i]=Integer.parseInt(st.nextToken());
		}
		st=new StringTokenizer(br.readLine());
		int B=Integer.parseInt(st.nextToken());
		int C=Integer.parseInt(st.nextToken());
		for (int i = 0; i < N; i++) {
			map[i]-=B;
			answer++;
			if(map[i]>0) {
				if(map[i]/C<1) {
					answer++;
				}else if(map[i]%C==0) {
					answer+=map[i]/C;
				}else {
					answer+=(map[i]/C)+1;
				}
			}
		}
		System.out.println(answer);
	}
}
