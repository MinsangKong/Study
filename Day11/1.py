#https://www.acmicpc.net/problem/1149
#백준 1149번 RGB거리
n = int(input())
arr = [] #빨강, 초록, 파랑
for i in range(n):
    arr.append(list(map(int, input().split())))
d = [[0]*3 for _ in range(1001)] 

for i in range(n):
    if i == 0:
        d[i] = arr[i]
    else:
        d[i][0] = arr[i][0]+min(d[i-1][1], d[i-1][2])
        d[i][1] = arr[i][1]+min(d[i-1][0], d[i-1][2])
        d[i][2] = arr[i][2]+min(d[i-1][0], d[i-1][1])
        
print(min(min(d[n-1][0], d[n-1][1]), d[n-1][2]))