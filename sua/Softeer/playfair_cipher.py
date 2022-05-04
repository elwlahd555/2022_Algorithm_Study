import sys

message = input()
inputkey = input()

alphabetList = [[0] * 5 for _ in range(5)]
alphabetDict = dict()

rowcnt = 0
colcnt = 0
# 키를 배열에 넣기
for i in range(len(inputkey)):

    if inputkey[i] in alphabetDict.keys():  # 이미 등록된 거면 skip
        continue
    else:
        alphabetList[rowcnt][colcnt] = inputkey[i]
        alphabetDict[inputkey[i]] = [rowcnt, colcnt]
        colcnt += 1
        if colcnt == 5:
            colcnt = 0
            rowcnt += 1

# 저장되지 않은 알파벳 뒤이어 저장하기
for j in range(0, 26):
    criteria = chr(ord("A") + j)
    if criteria == "J":
        continue
    if criteria in alphabetDict.keys():
        continue
    else:  # 저장되지 않은 알파벳이면 차례대로 배열에 저장
        alphabetList[rowcnt][colcnt] = criteria
        alphabetDict[criteria] = [rowcnt, colcnt]
        colcnt += 1
        if colcnt == 5:
            colcnt = 0
            rowcnt += 1

# 암호화하기
# 두개씩 나누기
prev = message[0]
cur = message[0] # 초기화 꼭 해주기
pairList = []  # 암호쌍 저장
for i in range(1, len(message)):

    cur = message[i]

    if prev == "pair":
        prev = cur
        if i == len(message) - 1:  # 마지막 단어
            prev = "last"

        continue

    if prev == cur:
        if prev == "X":
            pairList.append(prev + "Q")
        else:
            pairList.append(prev + "X")
        prev = cur
    else:
        pairList.append(prev + cur)
        prev = "pair"

if prev != "pair":  # 마지막 단어는 쌍이 되지 못했음
    pairList.append(cur + "X")  # 마지막은 X도 XX가 됨

# print(pairList)

# 쌍 암호화하기
# 두 글자가 같은행인가?
# 알파벳 좌표를 dict에 저장하고 찾는다.
# 같은 행 -> 오른쪽 한 칸 이동한 단어로 암호화
# (x+1)%5
# 같은 열에 존재 -> 아래쪽으로 한 칸 이동한 칸에 적힌 글자로 암호화
# 다른 행, 다른 열 위치 -> (0,1)과 (5,3)이면 (0,1)는(0,3) 됨, (5,3)은 (5,1 됨)

answerStr = ""

for i in pairList:  # 알파벳 쌍 꺼내기
    leftAlpha = i[0]
    rightAlpha = i[1]

    leftAlphaPos = alphabetDict[leftAlpha]
    leftX = leftAlphaPos[0]
    leftY = leftAlphaPos[1]
    rightAlphaPos = alphabetDict[rightAlpha]
    rightX = rightAlphaPos[0]
    rightY = rightAlphaPos[1]

    if leftX == rightX:
        newleftY = (leftY + 1) % 5
        newrightY = (rightY + 1) % 5
        newLeft = alphabetList[leftX][newleftY]
        newRight = alphabetList[rightX][newrightY]
        # answerList.append([newLeft,newRight])
        answerStr += newLeft + newRight
    elif leftY == rightY:
        newleftX = (leftX + 1) % 5
        newRightX = (rightX + 1) % 5
        newLeft = alphabetList[newleftX][leftY]
        newRight = alphabetList[newRightX][rightY]
        answerStr += newLeft + newRight
    else:
        newLeft = alphabetList[leftX][rightY]
        newRight = alphabetList[rightX][leftY]
        answerStr += newLeft + newRight

print(answerStr)












