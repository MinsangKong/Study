#https://www.acmicpc.net/problem/14496 최단 경로
#백준 14496번 그대, 그머가 되어
import sys
from heapq import heappop, heappush
input = sys.stdin.readline

a, b = map(int, input().split())
N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append((1, y))
    graph[y].append((1, x))

INF = sys.maxsize
dist = [INF] * (N + 1)
heap = [(0, a)]
dist[a] = 0
while heap:
    cost, u = heappop(heap)
    if dist[u] < cost:
        continue
    for w, v in graph[u]: #경로와 node를 따로 해야 listerror가 발생 안함
        if dist[v] > dist[u] + 1:
            dist[v] = dist[u] + 1
            heappush(heap, (dist[v], v))
print(-1) if dist[b] == INF else print(dist[b])
'''
맨 처음에 생각한 방식인데 계속 오류가 발생해서 bfs 방식으로 해결함
graph[x].append((1, y))로 적용하려면 반대편 graph[y].append((1, x))에 입력이 필요하고
다익스트라의 과정이 다르다.
'''
