#https://www.acmicpc.net/problem/2660
#백준 2660번 회장뽑기(플로이드)
#import sys
#input = sys.stdin.readline

n = int(input())
graph = [[51]*n for _ in range(n)]
while True:
    a,b = map(int, input().split())
    if a == -1 and b == -1:
        break
    graph[a-1][b-1] = 1
    graph[b-1][a-1] = 1
for i in range(n):
    graph[i][i] = 0
for k in range(n):
    for i in range(n):
        for j in range(n):
            if i == j :
                continue
            graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])
            
result = 51
idx = []
for i in range(n):
    check = 0
    for j in range(n):
        if graph[i][j] != 51 and check < graph[i][j]:
            check = graph[i][j]
            
    if result > check:
        result = check
        idx = []
        idx.append(i+1)
    elif max(graph[i]) == result:
        idx.append(i+1)
        
print(result, len(idx))
print(*idx)
'''
빠르게 풀려면 무조건 BFS를 활용해서 풀어야 한다
'''