#https://www.acmicpc.net/problem/1766
#백준 1766번 문제집(위상정렬)
#import sys
#input = sys.stdin.readline
import heapq

n, m = map(int, input().split())

graph = [[] for _ in range(n)]
indegree = [0]*n

for _ in range(m):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    indegree[b-1]+=1
    
q = []
for i in range(n):
    if indegree[i] == 0:
        heapq.heappush(q,i)
        
result = []

while q:
    now = heapq.heappop(q)
    
    result.append(now+1)
    for i in graph[now]:
        indegree[i] -= 1
        if indegree[i] == 0:
            heapq.heappush(q,i)
            
print(*result)