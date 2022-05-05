package com.solve.algorithm.java.programmers.sk;

import java.util.LinkedList;
import java.util.StringTokenizer;

public class BE_Server_개발_부문_2차_02 {
	private static class Point{
		String type;
		int t1,t2,x,y,z;
		public Point(String type, int t1, int t2, int x, int y, int z) {
			super();
			this.type = type;
			this.t1 = t1;
			this.t2 = t2;
			this.x = x;
			this.y = y;
			this.z = z;
		}
		
	}
	public static void main(String[] args) {
		String arr[]={"1","2","4","3","3","4","1","5"};
		String processes[]= {"read 1 3 1 2","read 2 6 4 7","write 4 3 3 5 2","read 5 2 2 5","write 6 1 3 3 9", "read 9 1 0 7"};
		System.out.println(solution(arr, processes));
	}
    public static String[] solution(String[] arr, String[] processes) {
        LinkedList<Point> read=new LinkedList<Point>();
        LinkedList<Point> write=new LinkedList<Point>();
        LinkedList<Point> process=new LinkedList<Point>();
        
        for (int i = 0; i < processes.length; i++) {
        	StringTokenizer st=new StringTokenizer(processes[i], " ");
        	if(st.nextToken().contentEquals("read")) {
        		read.add(new Point("read",Integer.parseInt(st.nextToken()),Integer.parseInt(st.nextToken()),Integer.parseInt(st.nextToken()),Integer.parseInt(st.nextToken()),0));
        	}else {
        		write.add(new Point("write",Integer.parseInt(st.nextToken()),Integer.parseInt(st.nextToken()),Integer.parseInt(st.nextToken()),Integer.parseInt(st.nextToken()),Integer.parseInt(st.nextToken())));
        	}
		}
        String[] answer = new String[read.size()+1];
        LinkedList<String> list=new LinkedList<String>();
        int time=0;
        int emptyTime=0;
        while(!read.isEmpty()||!write.isEmpty()||!process.isEmpty()) {

			if(process.size()>0) {
				if(check(process).equals("read")) {
					if(write.size()>0&&write.get(0).t1<=time) {
						
					}else if(read.size()>0&&read.get(0).t1<=time) {
						int size=read.size();
						for (int i = 0; i < size; i++) {
							if(read.get(0).t1<=time) {
								Point p=read.poll();
								process.add(p);
								String temp = "";
								for (int j = p.x; j <= p.y; j++) {
									temp += String.valueOf(arr[j]);
								}
								list.add(temp);
							}else {
								break;
							}
						}
					}
				}
			}else {
				if(write.size()>0&&write.get(0).t1<=time) {
					Point p = write.poll();
					process.add(p);
					for (int j = p.x; j <= p.y; j++) {
						arr[j]=String.valueOf(p.z);
					}
				}else if(read.size()>0&&read.get(0).t1<=time) {
					int size=read.size();
					for (int i = 0; i < size; i++) {
						if(read.get(0).t1<=time) {
							Point p=read.poll();
							process.add(p);
							String temp = "";
							for (int j = p.x; j <= p.y; j++) {
								temp += String.valueOf(arr[j]);
							}
							list.add(temp);
						}else {
							break;
						}
					}
				}
			}
			if(process.isEmpty()) {
				emptyTime++;
			}
			for (int i = 0; i < process.size(); i++) {
				process.get(i).t2--;
				if (process.get(i).t2 == 0) {
					process.remove(i);
					i--;
				}
			}
			time++;
        }
        for (int i = 0; i < list.size(); i++) {
			answer[i]=list.get(i);
		}
        answer[answer.length-1]=String.valueOf(time-emptyTime);
        return answer;
    }
	private static String check(LinkedList<Point> process) {
		for (int i = 0; i < process.size(); i++) {
			if(process.get(i).type.equals("write")) {
				return "write";
			}
		}
		return "read";
	}
}
