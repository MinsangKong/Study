#https://www.acmicpc.net/problem/1613
#백준 1613번 역사(플로이드)
#import sys
#input = sys.stdin.readline

n, k = map(int, input().split())
graph = [[0]*n for _ in range(n)]

for _ in range(k):
    a,b = map(int, input().split())
    graph[a-1][b-1] = -1
    graph[b-1][a-1] = 1
    
for k in range(n):
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            elif graph[i][j] == 0:
                if graph[i][k] == 1 and graph[k][j] == 1:
                    graph[i][j] = 1
                elif graph[i][k] == -1 and graph[k][j] == -1:
                    graph[i][j] = -1
                    
t = int(input())
for i in range(t):
    a, b = map(int, input().split())
    print(graph[a-1][b-1])