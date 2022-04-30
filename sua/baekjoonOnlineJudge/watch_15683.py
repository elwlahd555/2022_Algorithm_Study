import copy
# from collections import deque
# dfs 쓸 거니까 queue 쓰지마셈, queue쓰면 dfs하려니까 코드가 안 짜짐
N,M=map(int,input().split())

arr=[]
CCTV=[]

dx=[0,-1,0,1]
dy=[1,0,-1,0]

for i in range(N):
    rows=list(map(int, input().split()))
    arr.append(rows)
    for j in range(M):
        if 1<=rows[j]<=5:
            # 입력 받을 때 cctv 별 기본 방향 설정
            if rows[j]==1:
                direction=[0]
            elif rows[j]==2:
                direction=[0,2]
            elif rows[j]==3:
                direction=[0,1]
            elif rows[j]==4:
                direction=[0,1,2]
            elif rows[j]==5:
                direction=[0,1,2,3]

            CCTV.append([rows[j],(i,j),direction])


# print(CCTV)
cctvlen=len(CCTV)

def fill_arr(ix,iy,valdirerection,arr):
    # newarr = copy.deepcopy(arr)
    # 어차피 밑에서 arr 복원해주니까 입력받은 arr 에 그대로 값 씀
    for i in valdirerection:
        valx = ix
        valy = iy

        while True:
            valx = valx + dx[i]  # 계속 같은 방향으로 퍼짐
            valy = valy + dy[i]

            if 0 <= valx < N and 0 <= valy < M:
                if arr[valx][valy] ==0:
                    arr[valx][valy] = -1

                elif arr[valx][valy] == 6:
                    break
            else:
                break

    return arr

def turn_cctv(val,valdirerection):
    # cctv를 회전함
    # 방향 배열에서 1씩 더해주고 4로 나눈 나머지 저장해주면 됨
    newdirection = []
    if val[0] != 5:
        for i in valdirerection:
            newdirection.append((i + 1) % 4)
    else:  # 5는 그대로
        newdirection = valdirerection
    # newCCTV=[val[0], (ix, iy), newdirection]

    return newdirection

def get_area(arr):
    # 면적 구하기
    ans = 0

    for i in range(N):
        for j in range(M):
            if arr[i][j]==0:
                ans+=1

    return ans

def dfs(arr,CCTV,cnt):
    # 재귀함수 쓰기
    # 0번~N-1개 CCTV 호출, CCTV 스택에 저장(리스트),
    # 큐에 저장하니까 중간에 뺐다가 다시 넣어야되고 그래서 컨트롤이 힘듦
    # 0번 CCTV 상태를 저장하여 1번,2번 ..N-1 번 CCTV를 재귀적으로 호출함
    # 0번 CCTV가 할 수 있는 모든 방향에 대해 위에줄 행동을 반복
    # DFS 함수 수행 후에는 입력받았던 arr로 다시 돌려줌,

    global min_ans,cctvlen
    # print(CCTV)
    # print(arr)
    if cnt==cctvlen:
        # 모든 CCTV가 호출되었으면 반환
        # 백트래킹임. 뒤로 돌아가서 할 수 있는 모든 경우의 수를 탐색함
        # 게임 선택지처럼 되돌아가서 모든 경우의 수 확인해보기
        #  재귀함수 사용, 꼭 탈출함수 필요
        ans = get_area(arr)
        if min_ans > ans:
            min_ans = ans

        return

    temp = copy.deepcopy(arr)


    val = CCTV[cnt]
    numCCTV=val[0]


    # cctv 별 LOOP 수 줄여줌
    if numCCTV==1:
        forloop=4
    elif numCCTV==2:
        forloop=2
    elif numCCTV==3:
        forloop=4
    elif numCCTV==4:
        forloop=4
    elif numCCTV==5:
        forloop=1

    for i in range(forloop):
        ix = val[1][0]
        iy = val[1][1]
        valdirerection = val[2]

        newarr=fill_arr(ix,iy,valdirerection,temp) # 배열 채우기
        newdirection = turn_cctv(val, valdirerection)  # 방향 변환시키기
        val[2] = newdirection  # 새로운 방향 다음번에 쓰기
        # print(val[2])
        dfs(newarr,CCTV,cnt+1) # 다음 cctv 호출
        # val[2]=valdirerection # 이전 걸로 되돌리면 다음 방향으로 못 나감
        # print(val[2])
        temp=copy.deepcopy(arr)
        # 덮어써진 것을 지우고 원래것으로 되돌림, 그래야 새로운 방향에 대해 새로 탐색할 수 있음



    # print(min_ans)

min_ans=1e9
dfs(arr,CCTV,0)
print(min_ans)