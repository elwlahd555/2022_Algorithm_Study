package com.solve.algorithm.java.softeer;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class softeer623_비밀메뉴 {
	public static void main(String[] args) throws IOException {
		BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st=new StringTokenizer(br.readLine());
		int M=Integer.parseInt(st.nextToken());
		int N=Integer.parseInt(st.nextToken());
		int K=Integer.parseInt(st.nextToken());
		String secret="";
		String click="";
		st=new StringTokenizer(br.readLine());
		for (int i = 0; i < M; i++) {
			secret+=st.nextToken();
		}
		st=new StringTokenizer(br.readLine());
		for (int i = 0; i < N; i++) {
			click+=st.nextToken();
		}
		if(click.contains(secret)) {
			System.out.println("secret");
		}else {
			System.out.println("normal");
		}
	}
}
