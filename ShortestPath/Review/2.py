#https://www.acmicpc.net/problem/14221
#백준 14221번 편의점(다익스트라)
#import sys
#input = sys.stdin.readline
import heapq

def dijkstra(start):
    q = []
    heapq.heappush(q, (0,start))
    distance = [int(1e9)] * (n+1)
    distance[start] = 0
    num = int(1e9)
    while q :
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                if i[0] in cons and num > cost:
                    num = cost
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))
    return num

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]


for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a].append([b,c])
    graph[b].append([a,c])
    
p, q = map(int, input().split())
homes = list(map(int, input().split()))
cons = list(map(int, input().split()))

homes.sort()
result = int(1e9)
idx = 0
for i in homes:
    dist = dijkstra(i)
    if result > dist:
        result = dist
        idx = i
print(idx)
'''
pypy3로 제출해서 정답처리됨. homes 변수를 sort()하지 않고 하는 것이 더 빠를 줄 알았는데
변수가 난잡한지 sort()를 한 뒤에 다익스트라 처리를 하는 것이 더 빨랐다.
'''