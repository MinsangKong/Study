from heapq import *
import sys
INF = sys.maxsize

def dykstra(edge, start, v):
    dp = [INF] * (v+1)
    q = []
    
    for node, d in edge[start].items():
        dp[node] = d
        heappush(q, (d, node))

    while q:
        cur_dist, cur_node = heappop(q)
        if cur_node == start:
            return cur_dist

        if dp[cur_node] < cur_dist:
            continue
            
        for to_node, to_dist in edge[cur_node].items():
            dist = cur_dist + to_dist
            if dp[to_node] > dist:
                dp[to_node] = dist
                heappush(q, (dist, to_node))

    return INF

def solution():
    input = sys.stdin.readline
    v, e = map(int, input().split())
    edge = [{} for _ in range(v+1)]
    
    for _ in range(e):
        a, b, c = map(int, input().split())
        edge[a][b] = c
        
    result = INF
    for i in range(1, v+1):
        if result > dykstra(edge, i, v):
            result = dykstra(edge, i, v)

    print(result if result < INF else -1)

solution()