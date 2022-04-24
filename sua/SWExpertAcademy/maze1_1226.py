from collections import deque


dx=[0,1,0,-1]
dy=[1,0,-1,0]

for loop in range(10):
    tc=int(input())
    maze=[[-1]*16 for _ in range(16)]

    startp=deque()
    endp=(-1,-1)
    for i in range(16):
        rows=input()
        for j in range(16):
            maze[i][j] = int(rows[j])
            if rows[j]=='1' or rows[j]=='0':
                continue
            elif rows[j]=='2':
                # startp=(i,j)
                startp.append((i,j))
            elif rows[j]=='3':
                endp=(i,j)


    # print(maze)

    reachf=False

    while startp:
        cur=startp.popleft()
        curx=cur[0]
        cury=cur[1]

        for i in range(4):
            nx=curx+dx[i]
            ny=cury+dy[i]

            if 0<=nx<16 and 0<=ny<16:
                nextv=maze[nx][ny]
                if nextv==1:
                    continue
                elif nextv==0:
                    startp.append((nx,ny))
                    maze[nx][ny]=2 # 방문했으면 2써주긔
                elif nextv==3:
                    # 도착지임
                    reachf=True
                    break

        if reachf:
            print(f'#{tc} 1') # 도달가능
            break

    if not reachf:
        print(f'#{tc} 0') # 도달 불가