# 시뮬레이션 문제
import copy

# print(shark_pos)
# print(shark_priority)

n, m, k = map(int, input().split()) # n,m,k는 절대 for loop 변수로 쓰지말것
posx = [-1, 1, 0, 0]
posy = [0, 0, -1, 1]
arr = []
for i in range(n):
    # 상어 위치 표시..
    arr.append(list(map(int, input().split())))

# 상어 방향

# 1,2,3,4 위,아래,왼쪽,오른쪽
directions = list(map(int, input().split()))  # 상어 방향

priorities = [[] for _ in range(m)]
smell = [[[0, 0]] * n for _ in range(n)]

for i in range(m):  # 상어들의 우선순위 ?
    for j in range(4):  # 위,아래,왼쪽,오른쪽 # 여기 k로 바꾸면 절대 안됨... 입력으로 된 값들을 for loop 변수로 쓸 경우 값 바뀌기 때문에 ㄹㅇ주의해야함
        priorities[i].append(list(map(int, input().split())))


def update_smell():
    for i in range(n):
        for j in range(n):
            if smell[i][j][1] > 0:
                smell[i][j][1] -= 1
            if arr[i][j] != 0:  # 상어있으면 냄새뿌리기
                smell[i][j] = [arr[i][j], k]  # 상어 번호, 냄새지속시간


def move_sharks():
    # 상어야 이동하렴

    new_array = [[0] * n for _ in range(n)]

    for x in range(n):
        for y in range(n):
            if arr[x][y] != 0:  # 상어존재
                found = False
                direction = directions[arr[x][y] - 1]

                # 냄새 존재하지 않는 곳 확인
                for index in range(4):
                    nx = x + posx[priorities[arr[x][y] - 1][direction - 1][index] - 1]
                    ny = y + posy[priorities[arr[x][y] - 1][direction - 1][index] - 1]

                    if 0 <= nx < n and 0 <= ny < n:
                        if smell[nx][ny][1] == 0:  # 냄새가 존재하지 않는 곳이면
                            # 상어 방향 이동
                            directions[arr[x][y] - 1] = priorities[arr[x][y] - 1][direction - 1][index]  # 바뀐 방향으로 저장
                            if new_array[nx][ny] == 0:
                                # 상어 없으면 들어감
                                new_array[nx][ny] = arr[x][y]
                            else:
                                # 그 칸에 있는 상어보다 내 번호가 더 작으면 들어감
                                new_array[nx][ny] = min(new_array[nx][ny], arr[x][y])
                            found = True
                            break

                if found:
                    continue

                # 주변에 냄새 남아있으면 자신의 냄새가 있는 곳으로 이동

                for index in range(4):
                    nx = x + posx[priorities[arr[x][y] - 1][direction - 1][index] - 1]
                    ny = y + posy[priorities[arr[x][y] - 1][direction - 1][index] - 1]
                    if 0 <= nx < n and 0 <= ny < n:
                        if smell[nx][ny][0] == arr[x][y]:  # 자신의 냄새가 있는곳
                            directions[arr[x][y] - 1] = priorities[arr[x][y] - 1][direction - 1][index]  # 바뀐 방향으로 저장
                            new_array[nx][ny] = arr[x][y]
                            break

    return new_array


time = 0

while True:

    update_smell()
    new_array = move_sharks()
    arr = new_array  # 맵 업데이트
    time += 1

    check = True
    for i in range(n):
        for j in range(n):
            if arr[i][j] > 1:
                check = False

    if check:
        print(time)
        break
    if time >= 1000:
        print(-1)
        break
