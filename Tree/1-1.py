import sys
input = sys.stdin.readline
from collections import deque

def bfs(idx):
    visited = [-1]*(n+1)
    visited[idx] = 0
    q = deque([idx])
    while q :
        now = q.popleft()
        
        for _next,dist in graph[now]:
            if visited[_next] == -1:
                visited[_next] = dist+visited[now]
                q.append(_next)
                
    node, diameter = 0, 0
    for i in range(1,n+1):
        if diameter < visited[i]:
            node = i
            diameter = visited[i]
    return node, diameter

n = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(n):
    data = list(map(int, input().split()))
    idx = data[0]
    for i in range(1,len(data)-1,2):
        node, dist = data[i],data[i+1]
        graph[idx].append([node,dist])
        
target,_ = bfs(1)
_, result= bfs(target)

print(result)