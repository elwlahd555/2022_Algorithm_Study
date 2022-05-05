import sys

N = int(input())  # 소비자 수
customerArr = [[] for _ in range(N)]  # 소비자 별 각 제안을 저장함
max_car_size = -1  # 최대 차 사이즈만큼만 for loop 돌리기

for i in range(N):
    customer = list(map(int, input().split()))  # 고객 제안 정보
    numProposal = customer[0]  # 제안 수
    paircnt = 1

    for j in range(numProposal):
        pairarr = []
        if customer[paircnt] > max_car_size:  # 가장 큰 차 크기 구하기
            max_car_size = customer[paircnt]
        pairarr.append(customer[paircnt])
        pairarr.append(customer[paircnt + 1])
        paircnt += 2
        customerArr[i].append(pairarr)

M = int(input())  # 시나리오 개수 구하기
input_scenario = list(map(int, input().split()))  # Q원 이상의 매출을 낼 수 있는 신차의 최소크기 구하기
# 다이나믹 프로그래밍이라 인덱스로 배열에 접근-> 그래서 그런지 정렬해서 주지도 않았음

# Q 가 되기위한 차의 최소크기는 입력으로 받은 차의 크기 범위 내이다.
# 1~ 입력 받은 차 크기 max 값 - for loop 돌림

# 소비자가 십만, 제안이 오십만, 500억번 for loop 다 돌면 시간 초과
# 다이나믹 프로그래밍

# 차 크기가 DP일때 만들 수 있는 최대 매출 구하기
# 21원 이상 벌려면 최소크기는 ?


max_car_size += 1
dpArr = [-1] * max_car_size
for dp in range(1, max_car_size):
    dpmax = 0  # dp 별 최대금액
    for j in range(len(customerArr)):  # 제안 정보
        customerMaxMoney = 0  # 각 손님별 받을 수 있는 제안의 최대 매출액
        for cu in customerArr[j]:  # 손님 별 dp 이하 차 사이즈를 제안하면서, 최대 매출을 얻을 수 있는 제안 수락
            cuCarSize = cu[0]  # 손님이 제안한 차 크기
            if cuCarSize <= dp:
                if customerMaxMoney < cu[1]:  # 현재 저장된 최대 금액보다 크면 갱신
                    customerMaxMoney = cu[1]
        dpmax += customerMaxMoney  # 손님마다 최대금액을 더해줌

    dpArr[dp] = dpmax

# Q 원 이상의 매출액 정리

print(dpArr)

answerArr = []

for i in range(len(input_scenario)):
    breakFlag = False
    for j in range(1, len(dpArr)):
        if dpArr[j] >= input_scenario[i]:  # Q원 이상의 매출을 낼 수 있는 경우 신차의 최소 크기
            answerArr.append(j)
            breakFlag = True
            break
    # Q원 이상의 매출을 낼 수 없다면 -1
    if not breakFlag:
        answerArr.append(-1)

# 출력하기
for i in range(len(answerArr)):
    print(answerArr[i], end=" ")





