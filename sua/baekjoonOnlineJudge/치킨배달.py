from itertools import combinations

def find_chicken_dist(chicken_list):
    chicken_dist_sum = 0
    for j in home_location:
        min_val = 1e9
        for k in chicken_list:
            dis = abs(j[0] - k[0]) + abs(j[1] - k[1])
            if min_val > dis:
                min_val = dis
        chicken_dist_sum += min_val
    return chicken_dist_sum


n,m=map(int,input().split())
arr=[[0]*(n+1) for _ in range(n+1)]
chicken_store=[]
home_location=[]

for i in range(1,n+1):
    row=list(map(int,input().split()))
    for j in range(n):
        if row[j]==2: #치킨집
            chicken_store.append((i,j+1))
        elif row[j]==1:#집
            home_location.append((i,j+1))

chicken_list= list(combinations(chicken_store,m))
# print(chicken_list)

# copy_arr=copy.deepcopy(arr)
min_chicken_list_sum=1e9
min_chicken_store=[]
for i in chicken_list:

    dist=find_chicken_dist(i)
    if min_chicken_list_sum>dist:
        min_chicken_list_sum=dist
        min_chicken_store=i


print(min_chicken_list_sum)
# print(min_chicken_store)