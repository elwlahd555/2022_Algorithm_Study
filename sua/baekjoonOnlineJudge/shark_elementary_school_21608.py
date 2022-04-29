N = int(input())
inputarr = [[0] * 2 for _ in range(N * N)]
arr = [[-1] * N for _ in range(N)]
fav_list = [[0] for _ in range(N * N)]
fav_name = [[0] for _ in range(N * N)]

for i in range(N * N):
    rows = list(map(int, input().split()))
    student = rows[0] - 1
    inputarr[i][0] = student  # 학생 번호 -1 로 입력.
    fav_arr = []
    for j in range(4):
        fav_arr.append(rows[j + 1] - 1)
    fav_name[student] = fav_arr

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def simulation(N, inputarr, arr):
    for i in range(N * N):
        student = inputarr[i][0]
        # 인접칸 중 좋아하는 학생 수 세기
        max_fav = -1
        max_fav_pos = (-1, -1)
        max_blank_fav = -1
        # max_blank_pos=(-1,-1)
        for cx in range(N):
            for cy in range(N):
                if arr[cx][cy] != -1:
                    continue
                fav = 0
                blank_fav = 0
                for lk in range(4):
                    nx = cx + dx[lk]
                    ny = cy + dy[lk]
                    if 0 <= nx < N and 0 <= ny < N:

                        if arr[nx][ny] in fav_name[student]:
                            fav += 1
                        elif arr[nx][ny] == -1:
                            blank_fav += 1
                if max_fav <= fav:
                    if max_fav == fav:  # 좋아하는 학생이 인접한 칸이 여러개
                        if max_blank_fav < blank_fav:
                            # 비어있는 칸이 가장 많은 칸으로 정함
                            max_blank_fav = blank_fav
                            max_fav_pos = (cx, cy)
                    else:  # 좋아하는 학생이 인접한 칸에 가장 많은 칸
                        max_fav = fav
                        max_fav_pos = (cx, cy)
                        max_blank_fav = blank_fav
        ix = max_fav_pos[0]
        iy = max_fav_pos[1]
        arr[ix][iy] = student

    # print(max_fav)
    # print(max_fav_pos)

    # for ax in range(N):
    #     for ay in range(N):
    #         print(arr[ax][ay] + 1, end=' ')
    #     print()

    return arr


arr = simulation(N, inputarr, arr)
# print(arr)

# 학생 만족도 구하기

ans = 0
for i in range(N):
    for j in range(N):
        student = arr[i][j]
        fav_sum = 0
        for lk in range(4):
            nx = i + dx[lk]
            ny = j + dy[lk]

            if 0 <= nx < N and 0 <= ny < N:
                if arr[nx][ny] in fav_name[student]:
                    fav_sum += 1
        if fav_sum > 0:
            ans += pow(10, fav_sum - 1)
        # print(fav_sum)
        # print(ans)

print(ans)
