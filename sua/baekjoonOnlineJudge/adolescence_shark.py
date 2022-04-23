import copy

posx = [-1, -1, 0, 1, 1, 1, 0, -1]
posy = [0, -1, -1, -1, 0, 1, 1, 1]


def possible_path_for_shark(shark_loc, shark_dirc, arr):
    # 상어가 갈 수 있는 길 찾기
    nx = shark_loc[0]
    ny = shark_loc[1]

    # 상어가 갈 수 있는 위치 다 저장
    visitable_place = []
    for i in range(4):
        nx += posx[shark_dirc]
        ny += posy[shark_dirc]

        if 0 <= nx < 4 and 0 <= ny < 4:
            if arr[nx][ny] != -1:
                visitable_place.append((nx, ny))

    return visitable_place


def find_fish_loc(arr, target):
    idx = (-1, -1)
    for i in range(4):
        for j in range(4):
            if arr[i][j] == target:
                return (i, j)
    return idx


def move_all_fishes(arr, dirc,nowx,nowy):
    for i in range(1, 17):
        # 물고기 움직인다
        # 물고기 좌표찾기
        fish_loc = find_fish_loc(arr, i)
        if fish_loc != (-1, -1):
            fish_x = fish_loc[0]
            fish_y = fish_loc[1]
            fish_direction = dirc[fish_x][fish_y]

            for k in range(8):
                nx = fish_x + posx[fish_direction]
                ny = fish_y + posy[fish_direction]
                if 0 <= nx < 4 and 0 <= ny < 4:
                    if not (nx==nowx and ny==nowy):
                        dirc[fish_x][fish_y] = fish_direction
                        arr[nx][ny], arr[fish_x][fish_y] = arr[fish_x][fish_y], arr[nx][ny]
                        dirc[nx][ny], dirc[fish_x][fish_y] = dirc[fish_x][fish_y], dirc[nx][ny]
                        break


                fish_direction = (fish_direction + 1) % 8


def dfs(arr, dirc, shark_loc, ans):
    global result
    arr = copy.deepcopy(arr)
    dirc = copy.deepcopy(dirc)
    shark_x = shark_loc[0]
    shark_y = shark_loc[1]

    ans += arr[shark_x][shark_y]
    arr[shark_x][shark_y] = -1
    shark_dirc = dirc[shark_x][shark_y]

    move_all_fishes(arr, dirc,shark_x,shark_y)
    visitable_path = possible_path_for_shark(shark_loc, shark_dirc, arr)

    if len(visitable_path) == 0:
        result = max(result, ans)
        return

    for w in visitable_path:
        shark_x = w[0]
        shark_y = w[1]

        shark_location = (shark_x, shark_y)
        dfs(arr, dirc, shark_location, ans)


# print(arr)
# print(dirc)

n = 4
arr = [[0] * n for _ in range(n)]
dirc = [[0] * n for _ in range(n)]

for i in range(n):
    rows = list(map(int, input().split()))
    cnt = 0
    for j in range(0, 7, 2):
        arr[i][cnt] = rows[j]
        dirc[i][cnt] = rows[j + 1] - 1
        cnt += 1

result = 0
dfs(arr, dirc, (0, 0), 0)
print(result)
