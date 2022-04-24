import copy
from collections import deque

# 풀이 2번째

possible_walls=[]

def build_walls(copyarr, cnt,startrow,y):

    if cnt>=3:
        coparr = copy.deepcopy(copyarr)
        possible_walls.append(coparr)
        # 카피 안하면 밑에서 다시 되돌리는 작업때문에 무용지물됨..
        return
    for i in range(startrow,n):
        if i==startrow:
            startcol=y
        else:
            startcol=0
        for j in range(startcol,m):
            if copyarr[i][j]==0:
                cnt+=1
                copyarr[i][j]=1
                build_walls(copyarr, cnt,i,j+1)
                cnt-=1
                copyarr[i][j]=0


dx=[0,1,0,-1]
dy=[1,0,-1,0]

def spread_virus(copyarr,viruslist):
    for vr in viruslist:
        vrq=deque()
        vrx=vr[0]
        vry=vr[1]
        vrq.append((vrx,vry))
        while vrq:
            val=vrq.popleft()
            valx=val[0]
            valy=val[1]

            for i in range(4):
                nx=valx+dx[i]
                ny=valy+dy[i]

                if 0<=nx<n and 0<=ny<m:
                    if copyarr[nx][ny]==0:
                        vrq.append((nx,ny))
                        copyarr[nx][ny]=2
    return copyarr

def max_safety_area(resarr):
    area=0
    for i in range(n):
        for j in range(m):
            if resarr[i][j]==0:
                area+=1

    return area

def labs():

    arr = [[0] * m for _ in range(n)]
    viruslist = []
    for i in range(n):
        rows = list(map(int, input().split()))
        for j in range(m):
            if rows[j] == 2:
                viruslist.append((i, j))
            arr[i][j] = rows[j]

    # print(arr)

    ans=0
    copyarr=copy.deepcopy(arr)
    build_walls(copyarr,0,0,0)
    for possarr in possible_walls:
        resarr=spread_virus(possarr,viruslist)
        ans=max(ans,max_safety_area(resarr))

    print(ans)



n, m = map(int, input().split())
labs()



