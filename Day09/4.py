#https://www.acmicpc.net/problem/9095
#백준 9095번 1,2,3 더하기
n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
arr_max = max(arr)    
d = [0] * (arr_max+1)
d[1] = 1
d[2] = 2
d[3] = 4
for i in range(4, arr_max+1):
    d[i] = d[i-1]+d[i-2]+d[i-3]
    
for i in arr:
    print(d[i])