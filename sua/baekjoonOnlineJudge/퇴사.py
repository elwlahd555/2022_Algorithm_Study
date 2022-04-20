# 7
# 3 10
# 5 20
# 1 10
# 1 20
# 2 15
# 4 40
# 2 200

n=int(input())

arr=[]
dist=[0]*n
for i in range(n):
    rows=list(map(int,input().split()))
    arr.append((rows[0],rows[1]))
    if i+rows[0]-1<n:
        dist[i]=rows[1]


# print(arr)
# print(dist)


for j in range(n):
    period=arr[j][0] # 기간
    for k in range(j+1, n):
        if j+period<=k:
            if dist[k]!=0: # -1은 상담 못하는 날
                dist[k]=max(dist[k],dist[j]+arr[k][1])

# print(dist)
print(max(dist))