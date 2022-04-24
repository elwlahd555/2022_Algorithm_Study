from collections import deque

n = int(input())  # 보드 nXn
k = int(input())  # 사과 수
board = [[0] * n for _ in range(n)]

for _ in range(k):
    ax, ay = map(int, input().split())  # 사과 위치
    board[ax-1][ay-1] = 1  # 사과는 1

L = int(input())  # 뱀 방향 변환 횟수

move_plan = deque()
for _ in range(L):
    inp = input().split()
    move_plan.append((int(inp[0]), inp[1]))

# print(move_plan)

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def simulate():

    snake_pos = deque()
    snake_pos.append([0, 0])  # x,y,방향
    # 0 위 1 왼쪽  2 아래  3 오른쪽
    board[0][0] = 2  # 뱀 위치
    snake_dirc = 3  # 오른쪽
    time = 0

    next_move = move_plan.popleft()

    while True:

        v = snake_pos.popleft()
        snake_x = v[0]
        snake_y = v[1]

        nx = snake_x + dx[snake_dirc]
        ny = snake_y + dy[snake_dirc]
        if 0 <= nx < n and 0 <= ny < n:
            if board[nx][ny] == 1:  # 사과있다..
                snake_pos.appendleft([snake_x, snake_y])
                snake_pos.appendleft([nx, ny])

                board[nx][ny] = 2  # 뱀 위치 저장
            elif board[nx][ny]==2: # 내 몸이다
                print(time+1)
                break
            else:  # 사과 없다
                snake_pos.appendleft([snake_x, snake_y])
                snake_pos.appendleft([nx, ny])
                board[nx][ny] = 2
                tail = snake_pos.pop()  # 꼬리 없애줌
                board[tail[0]][tail[1]] = 0  # 빈칸 처리..
        else:
            # 경계를 벗어남
            print(time+1)
            break

        time+=1

        if next_move[0] == time:
            nextp= next_move[1]
            if nextp=="D":
            # 오른쪽 90도 턴
                if snake_dirc==0:
                    snake_dirc=3
                else:
                    snake_dirc= (snake_dirc-1)%4
            else:
                # 왼쪽 90도 턴
                snake_dirc=(snake_dirc+1)%4
            if len(move_plan)!=0:
                next_move=move_plan.popleft()

simulate()