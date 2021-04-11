#https://www.acmicpc.net/problem/1058 최단경로
#백준 1058번 친구(플로이드, 그래프 이론)
#import sys
#input = sys.stdin.readline
n = int(input())
s = []
visited = [[0] * n for i in range(n)]

for i in range(n):
    s.append(list(input()))
    
for k in range(n):
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if s[i][j] == "Y" or (s[i][k] == "Y" and s[k][j] == "Y"):
                visited[i][j] = 1
result = 0
for i in range(n):
    cnt = 0
    for j in range(n):
        if visited[i][j] == 1:
            cnt += 1
    result = max(result, cnt)
print(result)