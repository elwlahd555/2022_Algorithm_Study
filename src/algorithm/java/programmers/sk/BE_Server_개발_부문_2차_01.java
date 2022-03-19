package algorithm.java.programmers.sk;

import java.util.ArrayList;
import java.util.Collections;

public class BE_Server_개발_부문_2차_01 {
	public static void main(String[] args) {
		String goods[]={"abcdeabcd","cdabe","abce","bcdeab"};
		System.out.println(solution(goods));
	}
    public static String[] solution(String[] goods) {
        ArrayList<ArrayList<String>> list=new ArrayList<ArrayList<String>>();
        for (int i = 0; i < goods.length; i++) {
        	list.add(new ArrayList<String>());
		}
        for (int i = 0; i < goods.length; i++) {
			int size=0;
			while(list.get(i).size()==0&&goods[i].length()>size) {
				size++;
				for (int j = 0; j < goods[i].length(); j++) {
					if(j+size>goods[i].length()) {
						break;
					}
					String sub=goods[i].substring(j, j+size);
					if(check(i,sub,goods)&&!list.get(i).contains(sub)) {
						list.get(i).add(sub);
					}
				}
			}
		}
        for (int i = 0; i < list.size(); i++) {
			Collections.sort(list.get(i));
		}
        String[] answer = new String[goods.length];
        for (int i = 0; i < list.size(); i++) {
        	String temp="";
        	if(list.get(i).size()==0) {
        		temp="None";
        	}
			for (int j = 0; j < list.get(i).size(); j++) {
				if(!temp.equals("")) {
					temp+=" ";
				}
				temp+=list.get(i).get(j);
			}
			answer[i]=temp;
		}
        return answer;
    }
	private static boolean check(int cnt, String sub, String[] goods) {
		for (int i = 0; i < goods.length; i++) {
			if(cnt==i) {
				continue;
			}
			if(goods[i].contains(sub)) {
				return false;
			}
		}
		return true;
	}
}
