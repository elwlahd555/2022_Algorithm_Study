from itertools import combinations
import copy


def spread_virus(copy_arr,x,y):  # 바이러스 퍼뜨리기

    for i in range(4):
        dx = x + posx[i]
        dy = y + posy[i]

        if dx >=1 and dy >=1 and dx <= n and dy <= m :  # 범위 안에 있으면 전염

            if copy_arr[dx][dy] == 0:
                copy_arr[dx][dy] = 2  # 전염시킴

                spread_virus(copy_arr, dx, dy)

    return copy_arr

def measure_safety_zone(copy_arr):
    cnt=0
    for i in range(1,n+1):
        for j in range(1,m+1):
            if copy_arr[i][j]==0:
                cnt+=1

    return cnt



n,m=map(int,input().split())
arr=[[0]*(m+1) for _ in range(n+1)]
wall_loc=[]
virus_loc=[]
for i in range(n):
    row=list(map(int,input().split()))

    for j in range(m):
        arr[i+1][j+1]=row[j]
        if row[j]==0:
            wall_loc.append((i+1,j+1)) #전체 위치 저장해서 이 중 3개만 벽으로 뽑음.
        if row[j]==2 : #바이러스다
            virus_loc.append((i+1,j+1))

three_wall=list(combinations(wall_loc,3))
copy_arr=copy.deepcopy(arr)

posx = [0, 1, 0, -1]
posy = [1, 0, -1, 0]

max_safety_zone=-1
max_arr=[]
for i in three_wall:
    copy_arr = copy.deepcopy(arr)
    for j in i:
        if arr[j[0]][j[1]]==0: #빈 곳인지 확인 필요
            copy_arr[j[0]][j[1]]=1 #벽 세우기

    for i in virus_loc: # 바이러스 퍼뜨리기
        x = i[0]
        y = i[1]

        copy_arr=spread_virus(copy_arr,x,y)

    res=measure_safety_zone(copy_arr)
    if max_safety_zone<res:
        max_arr=copy_arr
        max_safety_zone=res
    # max_safety_zone=max(max_safety_zone, measure_safety_zone(copy_arr))


print(max_safety_zone)