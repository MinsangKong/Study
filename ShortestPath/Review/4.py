#https://www.acmicpc.net/problem/4485
#백준 4485번 녹색 옷 입은 애가 젤다지(다익스트라)
#import sys
#input = sys.stdin.readline
import heapq
INF = int(1e9)

def dijkstra(start):
    distance = [[INF]*n for _ in range(n)]
    distance[start][start] = 0
    direction = [(1,0),(-1,0),(0,1),(0,-1)]
    q = []
    heapq.heappush(q, (graph[0][0],0,0))
    while q:
        dist, x, y = heapq.heappop(q)
        for a,b in direction:
            dx = x+a
            dy = y+b
            if 0 <= dx < n and 0 <= dy < n:
                cost = dist+graph[dx][dy]
                if distance[dx][dy] > cost :
                    if dx == n-1 and dy == n-1:
                        return cost
                    distance[dx][dy] = cost
                    heapq.heappush(q, (cost, dx,dy))
idx = 1
while True:
    n = int(input())
    if n == 0:
        break
    graph = []
    
    for _ in range(n):
        graph.append(list(map(int, input().split())))
    result = dijkstra(0)
    print("Problem %d: %d" %(idx, result))
    idx+=1