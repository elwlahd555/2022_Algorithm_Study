
from collections import deque

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def is_reachable(arr,current_x,current_y,shark_size):

    n=len(arr[0])
    q=deque()
    visited=[[-1]*n for _ in range(n)]
    dist=[[1e9]*n for _ in range(n)]
    q.append((current_x,current_y))
    visited[current_x][current_y]=1
    dist[current_x][current_y]=0
    while q:
        x,y=q.popleft()

        for i in range(4):
            px=x+dx[i]
            py=y+dy[i]
            if 0<=px<n and 0<=py<n:

                    if visited[px][py]!=1:
                        if arr[px][py]<=shark_size:
                            q.append((px,py))
                            dist[px][py]=min(dist[px][py],dist[x][y]+1)
                        visited[px][py]=1

    min_dist=1e9
    shortest_xy=(-1,-1)
    for er in range(n):
        for ere in range(n):
            if arr[er][ere]!=0  and arr[er][ere]<shark_size:
                dist_v=dist[er][ere]
                if dist_v != 0 and dist_v!=1e9:
                    if min_dist>dist_v:
                        shortest_xy=(er,ere)
                        min_dist=dist_v


    return shortest_xy, min_dist

def bfs(n,arr,baby_shark):
    shark_size=2
    num_feed=0
    time=0
    while baby_shark:
        pos=baby_shark.popleft()
        x=pos[0]
        y=pos[1]

        # prey_x,prey_y=find_prey(arr,shark_size)
        shortest_xy,min_dist=is_reachable(arr,x,y,shark_size)
        st_x=shortest_xy[0]
        st_y=shortest_xy[1]
        if st_x!=-1 and st_y!=-1 and min_dist!=1e9:
            # arr[st_x][st_y]=0
            time+=min_dist
            # arr[st_x][st_y]=9
            baby_shark.append((st_x,st_y))
            arr[x][y]=0
            num_feed+=1
            if num_feed==shark_size:
                shark_size+=1
                num_feed=0

    return time


if __name__ == '__main__':

    n=int(input())
    arr = [[0]*n for _ in range(n)]

    baby_shark=deque()


    for rows in range(n):
        rv= list(map(int,input().split()))
        for col in range(n):

            if rv[col]==9:
                baby_shark.append((rows,col))
            else:
                arr[rows][col] = rv[col]

    print(bfs(n,arr,baby_shark))



