from itertools import permutations

n= int(input())
arr=list(map(int,input().split()))

# addition,subtraction,multiplication,division=map(int,input().split())
rows=list(map(int,input().split())) # 중복 제거
operation_list=[]
for i in range(4):
    if rows[i]!=0: # 연산 있을때만 더함
        temp=[i]*rows[i] # 연산 개수만큼 리스트에 넣음. 0,1,2,3 으로 연산 구별
        operation_list.extend(temp)

selected_operations=list(permutations(operation_list,n-1))
selected_operations=list(set(selected_operations))
max_value=-1e9
min_value=1e9

for i in range(len(selected_operations)):
    sum=arr[0]
    cur_opers_list = selected_operations[i]
    for j in range(1,len(arr)):
        oper= cur_opers_list[j-1]
        if oper==0: # 덧셈
            sum=sum+arr[j]
        elif oper==1: # 뺄셈
            sum=sum-arr[j]
        elif oper==2: # 곱셈
            sum*=arr[j]
        else : #나눗셈
            if sum<0 or arr[j]<0:
                sum= -int(abs(sum)//abs(arr[j]))
            else:
                sum=int(sum//arr[j])


    max_value=max(max_value,sum)
    min_value=min(min_value,sum)


print(max_value)
print(min_value)