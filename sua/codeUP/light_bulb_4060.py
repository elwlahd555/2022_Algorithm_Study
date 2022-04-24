import copy
from collections import deque

def find_target(arr,index):
    for i in range(n):
        for j in range(m):
            if arr[i][j]==index:
                return (i,j)
    return None

def bfs(arr,cur, target):

    cnt = 0

    while True:
        bulb = deque()

        ret= find_target(arr,cur) # cur 찾기
        if ret==None:
            break
        else:
            cnt+=1
            retx=ret[0]
            rety=ret[1]
            bulb.append((retx, rety))
            arr[retx][rety] = target


        while bulb:
            val = bulb.popleft()
            valx = val[0]
            valy = val[1]

            for i in range(4):
                nx = valx + dx[i]
                ny = valy + dy[i]

                if 0 <= nx < n and 0 <= ny < m:
                    if arr[nx][ny] == cur:
                        arr[nx][ny] = target
                        bulb.append((nx,ny))

    return cnt


n,m=map(int,input().split())
arr=[]

for i in range(n):
    arr.append(list(map(int,input().split())))

# print(arr)

dx=[0,1,0,-1]
dy=[1,0,-1,0]

def simulation():
    copyarr=copy.deepcopy(arr) # 원래 배열 바꾸면 뒤에서 못쓰니까 카피해줌.

    on=bfs(copyarr,0,1) # 모든 전구를 켜기

    copyarr=copy.deepcopy(arr)

    off=bfs(copyarr,1,0) # 모든 전구를 끄기
    print(on,off)

simulation()