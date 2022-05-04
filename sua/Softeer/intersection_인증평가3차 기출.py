import sys
from collections import deque
import heapq

N = int(input())
A = []
B = []
C = []
D = []

for i in range(N):
    row = sys.stdin.readline().split()
    ti = int(row[0])
    wi = row[1].strip()
    print(ti, wi)
    if wi == "A":
        A.append([ti, wi])
    elif wi == "B":
        B.append([ti, wi])
    elif wi == "C":
        C.append([ti, wi])
    elif wi == "D":
        D.append([ti, wi])

# print(A)
# print(B)
# print(C)
# print(D)

# 위 : A
# 오른쪽 : B
# 아래 : C
# 왼쪽 : D

# C,B,A,D 순으로 오른쪽으로 감

cnt = 0
answer = []
A_front = [1e9+1, 1e9+1]
B_front = [1e9+1, 1e9+1]
C_front = [1e9+1, 1e9+1]
D_front = [1e9+1, 1e9+1]

move_flag=True # 차가 지나갔는가 플래그
while True:
    print(cnt)
    if len(A) == 0 and len(B) == 0 and len(C) == 0 and len(D) == 0:
        # 교차로에 차 존재하지 않으면 끝
        break
    if not move_flag:
        if A_front[0]!=1e9+1 or B_front[0]!=1e9+1 \
                or C_front[0]!=1e9+1\
                or D_front[0]!=1e9+1:
            move_flag=True
            continue
        # 지나간 차가 없다면 교착상태이므로 -1 추가해주고 종료
        heapq.heappush(answer, (A_front[0], A_front[1], -1))
        heapq.heappush(answer, (B_front[0], B_front[1], -1))
        heapq.heappush(answer, (C_front[0], C_front[1], -1))
        heapq.heappush(answer, (D_front[0], D_front[1], -1))
        break

    if len(A) != 0:
        A_front = A[0]
    else:
        A_front = [1e9+1, 1e9+1]  # 비어있다는 표시
    if len(B) != 0:
        B_front = B[0]
    else:
        B_front = [1e9+1, 1e9+1]
    if len(C) != 0:
        C_front = C[0]
    else:
        C_front = [1e9+1, 1e9+1]
    if len(D) != 0:
        D_front = D[0]
    else:
        D_front = [1e9+1, 1e9+1]

    move_flag=False # 한명이라도 지나갔으면,True로 바꿔줌.

    if len(A) != 0 and A_front[0] <= cnt and D_front[0] > cnt:
        # D비어있으면 A 지나감
        move_flag=True
        A.pop(0)  # 스택에서 제거
        heapq.heappush(answer, (A_front[0], A_front[1], A_front[0] + cnt))
    if len(B) != 0 and B_front[0] <= cnt and A_front[0] > cnt:
        # A비어있으면 B 지나감
        move_flag=True
        B.pop(0)  # 스택에서 제거
        heapq.heappush(answer, (B_front[0], B_front[1], B_front[0] + cnt))
    if len(C) != 0 and C_front[0] <= cnt and B_front[0] > cnt:
        # B비어있으면 C지나감
        move_flag=True
        C.pop(0)  # 스택에서 제거
        heapq.heappush(answer, (C_front[0], C_front[1], C_front[0] + cnt))
    if len(D) != 0 and D_front[0] <= cnt and C_front[0] > cnt:
        # C비어있으면 D 지나감
        move_flag=True
        D.pop(0)  # 스택에서 제거
        heapq.heappush(answer, (D_front[0], D_front[1], D_front[0] + cnt))

    cnt+=1

for hl in range(len(answer)):
    heap_ans = heapq.heappop(answer)
    print(heap_ans[2])
