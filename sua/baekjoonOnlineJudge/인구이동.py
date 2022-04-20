from collections import deque



n,l,r=map(int,input().split())
arr=[[]*n for _ in range(n)]
for i in range(n):
    rows=list(map(int,input().split()))
    for j in range(n):
        arr[i].append(rows[j])


dx=[0,1,0,-1]
dy=[1,0,-1,0]


def find_neightbors(arr):
    cnt = 0
    flag=False
    visited=[[False]*n for _ in range(n)]
    idx=0
    for i in range(n):
        for j in range(n):
            visited_list = []
            sum = 0
            if not visited[i][j]:
                q = deque()
                q.append((i, j))
                visited_list.append((i, j))

                while len(q)!=0:
                    pos=q.popleft()

                    x=pos[0]
                    y=pos[1]
                    visited[x][y] = True

                    for dir in range(4):
                        newx= x+dx[dir]
                        newy= y+dy[dir]

                        if newx>=0 and newy>=0 and newx<n and newy<n :
                            if not visited[newx][newy]:
                                if l<=abs(arr[x][y]-arr[newx][newy])<=r :
                                    visited[newx][newy]=True
                                    q.append((newx,newy))
                                    visited_list.append((newx, newy))
                                    # print((newx,newy))

            # print(visited_list)
            if len(visited_list)>=2:
                flag=True
                cnt+=1

                for neighbor in visited_list:
                    sum+=arr[neighbor[0]][neighbor[1]]
                    # print(arr[neighbor[0]][neighbor[1]])

                for neighbor in visited_list:
                    arr[neighbor[0]][neighbor[1]]=int(sum/len(visited_list)) # 소수점 버림을 안해주면 틀림
            elif len(visited_list)==1:
                idx+=1
    if idx==n*n:
        flag= False
    # print(arr)
    # print(cnt)
    return cnt,flag,arr

res=0
num=0
while 1:
    cntt,flag,arr=find_neightbors(arr)
    # print(flag)
    if not flag:
        break
    res+=cntt
    num+=1
# print(res)
print(num)