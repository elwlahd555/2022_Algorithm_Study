from collections import deque

N, L, R = map(int, input().split())
arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# def find_not_visited(visited):
#     for i in range(N):
#         for j in range(N):
#             if visited[i][j]==0:
#                 return (i,j)
#     return None


visited = [[0] * N for _ in range(N)]
no_move = True


def solution():
    # 시간 초과 -> 더 이상 이동 안하는 애들은 제외시켜야 함
    global no_move
    global visited

    time = 0
    while True:
        no_move = True
        visited = [[0] * N for _ in range(N)]
        idx = 0

        for i in range(N):  # 0 찾는 함수 따로 만들면 오래 걸림.
            for j in range(N):
                if visited[i][j] == 0:
                    q = deque()
                    visqx = i
                    visqy = j
                    visited[visqx][visqy] = 1
                    q.append((visqx, visqy))
                    united = []
                    united.append((visqx, visqy))

                    unite_move(q, united)
                    idx += 1

        if no_move or idx == N * N:
            print(time)
            break
        time += 1


def unite_move(q, united):
    total = 0
    global no_move
    while q:

        val = q.popleft()

        valx = val[0]
        valy = val[1]
        total += arr[valx][valy]

        for j in range(4):
            nx = valx + dx[j]
            ny = valy + dy[j]
            if 0 <= nx < N and 0 <= ny < N:
                if visited[nx][ny] == 0:
                    dif = abs(arr[nx][ny] - arr[valx][valy])
                    if L <= dif <= R:
                        q.append((nx, ny))
                        visited[nx][ny] = 1
                        united.append((nx, ny))
                        no_move = False

    for i in united:
        arr[i[0]][i[1]] = int(total / len(united))


# print(arr)


solution()