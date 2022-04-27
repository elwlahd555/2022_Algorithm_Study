N=int(input())

arr=list(map(int,input().split()))
operator=list(map(int,input().split()))
# 0번 덧셈, 1번 뺄셈, 2번 곱셈 3번 나눗셈
operator_list=[]
count_list=[]
min_val=1e9
max_val=-1e9

def dfs(idx, oper, arr, operator_list, operator):
    global min_val,max_val

    if idx==N-1:
        temp=arr[0]
        for i in range(N-1):
            if operator_list[i]==0:
                ans=temp+arr[i+1]
            elif operator_list[i]==1:
                ans=temp-arr[i+1]
            elif operator_list[i]==2:
                ans=temp*arr[i+1]
            else:

                if temp<0 or arr[i+1]<0:
                    ans=-int(abs(temp)/arr[i+1])
                else:
                    ans = int(temp / arr[i + 1])
            temp=ans

        min_val=min(min_val,ans)
        max_val=max(max_val,ans)

        return

    if operator[0]>0:
        operator[0] -= 1
        operator_list.append(0)
        dfs(idx + 1, oper, arr, operator_list, operator)
        operator[0] += 1
        operator_list.pop()
    if operator[1]>0:
        operator_list.append(1)
        operator[1] -= 1
        dfs(idx + 1, oper, arr, operator_list, operator)
        operator[1] += 1
        operator_list.pop()
    if operator[2]>0:
        operator_list.append(2)
        operator[2] -= 1
        dfs(idx + 1, oper, arr, operator_list, operator)
        operator[2] += 1
        operator_list.pop()
    if operator[3]>0:
        operator_list.append(3)
        operator[3] -= 1
        dfs(idx + 1, oper, arr, operator_list, operator)
        operator[3] += 1
        operator_list.pop()


dfs(0,0,arr,operator_list,operator)
print(max_val)
print(min_val)