#https://www.acmicpc.net/problem/1389
#백준 1389번 케빈 베이컨의 6단계 법칙(플로이드)
#import sys
#input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[101]*n for _ in range(n)]

for _ in range(m):
    a,b = map(int, input().split())
    graph[a-1][b-1] = 1
    graph[b-1][a-1] = 1
    
for k in range(n):
    for i in range(n):
        for j in range(n):
            if i == j :
                graph[i][j] = 0
            else:
                graph[i][j] = min(graph[i][j],graph[i][k]+graph[k][j])
                
result = 101
idx = 0
for i in range(n):
    if sum(graph[i]) < result:
        result = sum(graph[i])
        idx = i
        
print(idx+1)
'''
시간 효율성 면에서는 플로이드보다 bfs가 훨씬 빨랐다.
'''