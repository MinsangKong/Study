#https://www.acmicpc.net/problem/13911
#백준 13911번 집 구하기(다익스트라)
#import sys
#input = sys.stdin.readline
import heapq
INF = int(1e9)

def dijkstra(start):
    distance = [INF] * (v+1)
    distance[start] = 0
    q = []
    mac_check = INF
    star_check = INF
    heapq.heappush(q,(0,start))
    while q:
        dist, now = heapq.heappop(q)
        if now in macs:
            if dist < mac_check:
                mac_check = dist
        elif now in stars:
            if dist < star_check:
                star_check = dist
        if mac_check <= mac_limit and star_check <= star_limit:
            return mac_check+star_check
        for i in graph[now]:
            cost = dist+i[1]
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))
    return -1

v,e = map(int, input().split())
graph = [[] for _ in range(v+1)]


for _ in range(e):
    a,b,c = map(int, input().split())
    graph[a].append([b,c])
    graph[b].append([a,c])
    
mac_num, mac_limit = map(int, input().split())
macs = list(map(int, input().split()))
star_num, star_limit = map(int, input().split())
stars = list(map(int, input().split()))
result = INF
for i in range(1,v+1):
    if i not in macs and i not in stars:
        num = dijkstra(i)
        if num != -1 and result > num :
            result = num
print(result)
'''
알고리즘 자체는 맞지만 여러번 다익스트라를 처리하기 때문에 시간초과 발생
'''