n=int(input()) # 전체 상담 개수
t=[] # 각 상담을 완료하는 데 걸리는 기간
p=[] # 각 상담을 완료했을 때 받을 수 있는 금액
dp=[0]*(n+1) # 다이나믹 프로그래밍을 위한 1차원 dp 테이블 초기화
max_result=0

for i in range(n):
    x,y=map(int,input().split())
    t.append(x)
    p.append(y)

for j in range(n-1,-1,-1):
    time= j+t[j]
    # 상담이 기간 안에 끝나는 경우
    if time<=n: # 현재까지의 최고 이익 계산
        dp[j]=max(p[j]+dp[time],max_result)
        max_result=dp[j]

    else:
        # 상담이 기간을 벗어나는 경우
        dp[j]=max_result

print(max_result)