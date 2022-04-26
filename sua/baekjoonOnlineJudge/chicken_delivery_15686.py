

N,M=map(int,input().split())
arr=[]
for i in range(N):
    arr.append(list(map(int,input().split())))

num_chicken=0

# 집 저장하기
home_list=[] # 고정되는 건 미리 배열에 저장해놓자.
# N*N 반복문 돌지 않기 위해서.
for i in range(N):
    for j in range(N):
        if arr[i][j]==2:
            num_chicken+=1

        elif arr[i][j]==1:
            home_list.append((i,j))

# 0 빈칸, 1 집, 2 치킨집
# 치킨집 M개만 남겨야 함.

ans = 1e9

def get_chicken_dist(chicken_list,home_list): # 전역변수 쓰면 느리니까 자제함


    ck_sum=0 # 모든 집의 치킨 거리의 합
    for i in home_list:
        # 집이면 치킨거리 구하기
        ckmindist=1e9
        for ck in chicken_list:
            val=abs(ck[0]-i[0])+abs(ck[1]-i[1])
            ckmindist=min(ckmindist,val)
        ck_sum+=ckmindist
    return ck_sum



def dfs(ans,arr,cnt,startrow,y,home_list):
    # 전역변수 사용안하려고 다 지역변수로 받음.
    if cnt==M:
        # 치킨 거리 구하기
        chicken_list = []
        for i in range(N):
            for j in range(N):
                if arr[i][j] == 2:
                    chicken_list.append((i,j))

        return get_chicken_dist(chicken_list,home_list)

    for i in range(startrow,N): # 매번 0부터 돌면 시간초과됨. 여기 처리 잘 해줘야함

        if startrow==i: # 이미 지나간 인덱스 볼 필요 없음 !
            startcol=y
        else:
            startcol=0
        for j in range(startcol,N):
            if arr[i][j]==2: # 치킨집이다!
                arr[i][j]=0 # 개수 뺴기

                ans=min(ans,dfs(ans,arr,cnt-1,i,j+1,home_list))

                arr[i][j]=2 # 다시 복원

    return ans

ans=dfs(ans,arr,num_chicken,0,0,home_list)
print(ans)