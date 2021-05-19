#https://www.acmicpc.net/problem/1238
#백준 1238번 파티(다익스트라)
#import sys
#input = sys.stdin.readline
INF = int(1e9)
import heapq

def dijkstra(start, dp, graph):
    q = []
    heapq.heappush(q,(0,start))
    dp[start] = 0
    while q:
        dist,now = heapq.heappop(q)
        if dp[now] < dist:
            continue
        for i in graph[now]:
            cost = dist+i[1]
            if dp[i[0]] > cost:
                dp[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))
                
n,m,x = map(int, input().split())
start_graph = [[] for _ in range(n+1)]
end_graph = [[] for _ in range(n+1)]


for _ in range(m):
    a,b,c = map(int, input().split())
    end_graph[a].append([b,c])
    start_graph[b].append([a,c])
    
start_dp = [INF] * (n+1)
end_dp = [INF] * (n+1)
dijkstra(x,start_dp,start_graph)
dijkstra(x,end_dp,end_graph)
result = 0
for i in range(1,n+1):
    total = start_dp[i]+end_dp[i]
    if result < total:
        result = total
print(result)