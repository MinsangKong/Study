#https://www.acmicpc.net/problem/2910
#백준 2910번 빈도정렬 
n, c = map(int, input().split())
arr = list(map(int, input().split()))
arr_count = {} #key는 메세지, value:[빈도, 들어온 순서]
for i in range(n):
    if arr[i] in arr_count:
        arr_count[arr[i]][0] +=1
    else:
        arr_count[arr[i]] = [1,i]
        
l = lambda x : (-x[1][0], x[1][1])
result = sorted(arr_count.items(), key = l)
answer = []
for i in result:
    for j in range(i[1][0]):
        answer.append(str(i[0]))
        
print(" ".join(answer))