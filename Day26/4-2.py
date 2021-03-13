#https://www.acmicpc.net/problem/11724
#백준 11724번 연결 요소의 개수(그래프 이론,dfs, 사이클)
import sys
#input = sys.stdin.readline
def dfs(v):
    visited[v] = 1
    for i in range(1, n+1):
        if visited[i] == 0 and graph[v][i] == 1:
            dfs(i)

sys.setrecursionlimit(100000) 
n, m = map(int, input().split())
graph = [[0] * (n+1) for i in range(n+1)]
visited = [0] * (n+1)

for i in range(m):
    v1, v2 = map(int, input().split())
    graph[v1][v2] = 1
    graph[v2][v1] = 1

count = 0
for i in range(1, n+1):
    if visited[i] == 0:
        dfs(i)
        count += 1
print(count)
'''
root찾기로 해결 했을 경우에는 880ms, dfs로 해결했을 경우에는 696ms가 걸린다.
싸이클을 찾야하는 경우가 아니면 dfs나 bfs로 찾는 것이 효율적이다.
'''