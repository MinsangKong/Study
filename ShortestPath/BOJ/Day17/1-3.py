#https://www.acmicpc.net/problem/14496 최단 경로
#백준 14496번 그대, 그머가 되어
#기준을 어떻게 잡느냐에 따라서 결과가 달라진다.
import sys
import heapq
INF = 1e9
input = sys.stdin.readline
a, b = map(int, input().rstrip().split())
n, m = map(int, input().rstrip().split())
adj = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)
for _ in range(m):
    c1, c2 = map(int, input().rstrip().split())
    adj[c1].append(c2)
    adj[c2].append(c1) 
#책에 있는 방식으로 하려면 값이 정해져 있지 않은 경우, 2가지 모두 저장해 줘야한다.                       

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in adj[now]:
            cost = dist + 1
            if cost < distance[i]:
                distance[i] = cost
                heapq.heappush(q, (cost, i))

dijkstra(a)
if distance[b] == INF:
    print(-1)
else:
    print(distance[b])