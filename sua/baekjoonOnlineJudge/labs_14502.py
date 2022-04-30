
# 연구소 풀이 첫번째

dx=[0,1,0,-1]
dy=[1,0,-1,0]

def build_walls (cnt,startrow,idx):
    global ans

    if cnt==3:
        for i in range(n):
            for j in range(m):
                temp[i][j]=arr[i][j]

        # 바이러스 뿌리고 배열 원래대로 복원해줘야함.

        for i in range(n):
            for j in range(m):
                if temp[i][j]==2:
                    spread_virus(i,j)


        ans=max(ans,max_safety_area())

        # 중복인지 아닌지 걸러주는 작업 필요.. - 안하면 시간초과됨
        return
    for i in range(startrow,n):

        if i==startrow:
            startcol=idx
        else:
            startcol=0
        for j in range(startcol,m):
            if arr[i][j]==0:
                cnt+=1
                arr[i][j]=1

                build_walls(cnt,i,idx+1)
                # copyarr는 arr를 가리키고 있기때문에 copyarr 가 바뀌면 arr도 바뀜..그것이 바로 얕은 참조..
                # 카피 안하면 밑에서 다시 되돌리는 작업때문에 무용지물됨..
                # 배열을 복사하는 연산은 느리다..
                # 중복 방문안하기 위해서 탐색 범위 제외하고 해야함

                cnt-=1
                arr[i][j]=0



def spread_virus(x,y):

    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]

        if 0<=nx<n and 0<=ny<m:
            if temp[nx][ny]==0:
                temp[nx][ny]=2
                spread_virus(nx,ny)


def max_safety_area():
    area=0
    for i in range(n):
        for j in range(m):
            if temp[i][j]==0:
                area+=1

    return area






n, m = map(int, input().split())

arr = []
temp=[[0] * m for _ in range(n)]

for i in range(n):
    arr.append(list(map(int, input().split())))

ans=0
build_walls(0,0,0)

print(ans)