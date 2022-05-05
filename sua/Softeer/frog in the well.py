import sys

N, M = map(int, input().split())

W = list(map(int, input().split()))

closestArr = [[] for _ in range(N)]

for i in range(M):  # 친분 관계 저장
    a, b = map(int, input().split())
    closestArr[a - 1].append(b - 1)
    closestArr[b - 1].append(a - 1)

answer = 0  # 내가 최고라고 생각하는 회원 수

for i in range(N):
    wi = W[i]
    if len(closestArr[i]) == 0:
        answer += 1
        continue
    breakFlag = False
    for j in closestArr[i]:  # 친분 관계 중 내가 제일 무거운 거 드는가?
        if wi <= W[j]:  # 나와 같거나 나보다 더 무거운 거 드는 회원있음
            breakFlag = True
            break

    if not breakFlag:  # 나보다 쎈 애가 없음
        answer += 1

print(answer)

