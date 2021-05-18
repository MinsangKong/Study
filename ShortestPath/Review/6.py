#https://www.acmicpc.net/problem/1916
#백준 1916번 최소비용 구하기(다익스트라)
#import sys
#input = sys.stdin.readline
import heapq
INF = int(1e9)

def dijkstra(start, end):
    q = []
    distance[start] = 0
    heapq.heappush(q,[0,start])
    while q :
        dist, now = heapq.heappop(q)
        if now == end:
            return dist
        for i in graph[now]:
            cost = dist+i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,[cost,i[0]])

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a].append([b,c])
    
start, end = map(int, input().split())
print(dijkstra(start,end))
'''
의외로 if distance[now] < dist: 문을 작성하는 것이 30ms정도 더 느렸다.
            continue
'''