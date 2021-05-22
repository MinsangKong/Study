#https://www.acmicpc.net/problem/10159
#백준 10159번 저울(플로이드)
#import sys
#input = sys.stdin.readline
INF = int(1e9)

n = int(input())
m = int(input())

graph = [[INF]*n for _ in range(n)]

for i in range(n):
    graph[i][i] = 0
    
for _ in range(m):
    a,b = map(int, input().split())
    graph[a-1][b-1] = 1
    graph[b-1][a-1] = -1
    
for k in range(n):
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if graph[i][j] == INF :
                if graph[i][k] == 1 and graph[k][j] == 1:
                    graph[i][j] = 1
                elif graph[i][k] == -1 and graph[k][j] == -1:
                    graph[i][j] = -1
for i in range(n):
    cnt = 0
    for j in range(n):
        if graph[i][j] == INF:
            cnt+=1
    print(cnt)