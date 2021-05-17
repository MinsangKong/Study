#https://www.acmicpc.net/problem/1504
#백준 1504번 특정한 최단 경로(다익스트라)
#import sys
#input = sys.stdin.readline
import heapq
INF = int(1e9)

def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start))
    distance = [INF] * (n+1)
    distance[start] = 0
    while q :
        dist, now = heapq.heappop(q)
        for i in graph[now]:
            cost = dist+i[1]
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    print(distance)
    return distance

n,e = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(e):
    a,b,c = map(int, input().split())
    graph[a].append([b,c])
    graph[b].append([a,c])
    
v1, v2 = map(int, input().split())
one = dijkstra(1)
v1_ = dijkstra(v1)
v2_ = dijkstra(v2)
result = min(one[v1] + v1_[v2] + v2_[n], one[v2] + v2_[v1] + v1_[n])
print(result if result < INF else -1)