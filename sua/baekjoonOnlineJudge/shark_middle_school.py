# 완전탐색
import copy
from collections import deque

N,M= map(int,input().split())
arr=[]

for i in range(N):
    arr.append(list(map(int,input().split())))

dx=[0,1,0,-1]
dy=[1,0,-1,0]
visit = [[False]*N for _ in range(N)]

def find_max_block_group(arr,visit):

    max_block=-1e9
    max_block_list=[]
    max_rainbow_block=-1e9
    for i in range(len(arr)):
        for j in range(len(arr)):
            val=arr[i][j]
            if val==-1 or val==0 or val==-2: # 일반블록이 꼭 필요함
                continue
            cnt=0
            tempvisit=copy.deepcopy(visit) # 방문 확인 배열 카피
            valqueue=deque()
            valqueue.append((i,j))
            block_list=[]
            rainbow_cnt=0
            tempvisit[i][j]=True
            while valqueue:
                cnt+=1
                popval=valqueue.popleft()
                cx=popval[0]
                cy=popval[1]
                block_list.append((cx,cy))
                for lw in range(4):
                    nx=cx+dx[lw]
                    ny=cy+dy[lw]

                    if 0<=nx<N and 0<=ny<N:
                        if tempvisit[nx][ny]==False: # 방문 안했을때만 방문
                            if arr[nx][ny]==0 or arr[nx][ny]==val:
                                if arr[nx][ny]==0: # rainbox 블록 개수세기
                                    rainbow_cnt+=1
                                valqueue.append((nx,ny))
                                tempvisit[nx][ny]=True
                            else:# 검은 블록이거나 다른 일반블록이면 skip
                                continue

            if max_block==cnt: # 가장 큰 블록 그룹 찾기
                # 무지개 블록 수도 세야함
                if max_rainbow_block<rainbow_cnt:
                    max_block = cnt
                    max_rainbow_block = rainbow_cnt
                    max_block_list = block_list
                elif max_rainbow_block==rainbow_cnt:
                    # 기준 블록 처리를 안했슴.
                    max_block = cnt
                    max_rainbow_block = rainbow_cnt
                    max_block_list = block_list
            elif max_block<cnt:
                max_block=cnt
                max_rainbow_block=rainbow_cnt
                max_block_list=block_list


    return max_block_list

def remove_block(arr,block_list):
    for i in block_list:
        cx=i[0]
        cy=i[1]
        arr[cx][cy]=-2 # 블록을 제거한다. 제거된 곳은 -2이다.

    return arr


def apply_gravity(arr):
    # 행 거꾸로 시작해야함
    for i in range(N-2,-1,-1):
        for j in range(N-1,-1,-1):
            # 열마다 계산해서 중력 작용
            if arr[i][j]==-1 or arr[i][j]==-2:    # 검은색 블록 빼고 중력 작용
                continue
            chidx=(N-1,j)
            for lw in range(N-1,i,-1):
                # if arr[lw][j]==-2:
                #     chidx=(lw,j)
                # else: # 중간에 뭐가 있다. 그럼 그 위에 쌓는다.
                if arr[lw][j]!=-2:
                    chidx=(lw-1,j)
            arr[chidx[0]][chidx[1]],arr[i][j]=arr[i][j],arr[chidx[0]][chidx[1]]
    return arr

def rotate_clockwise90degree(arr):
    # 새로운 배열에 옮겨야함
    # 반시계 90도 방향 회전
    newarr=[[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            newarr[N-j-1][i]=arr[i][j]
    return newarr


def simulation(arr,visit):
    answer=0
    while True:
        max_block_list=find_max_block_group(arr,visit)
        # print(max_block_list)
        if len(max_block_list)<=1:
            # 더 이상 블록 그룹 없음
            break
        else: #점수얻기
            arr=remove_block(arr,max_block_list) # 블록 제거
            answer+=pow(len(max_block_list),2) # B의 2승 점수를 획득
            # 중력이 작용한다.
            arr=apply_gravity(arr)
            # 격자가 90도 반시계 방향으로 회전
            arr=rotate_clockwise90degree(arr)
            # 다시 중력 작용
            arr=apply_gravity(arr)

    return answer

print(simulation(arr,visit))