#Q40 숨바꼭질
import heapq
INF = int(1e9)

def dijkstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0,start))
    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]:
            continue
        
        for i in graph[now]:
            cost = dist+i[1]
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))

n, m = map(int, input().split())

graph = [[] for _ in range(n)]
distance = [INF]*n

for _ in range(m):
    a,b = map(int, input().split())
    graph[a-1].append([b-1,1])
    graph[b-1].append([a-1,1])
    
dijkstra(0)
idx = 1
result = 0
cnt = 0

for i in range(n):
    if distance[i] > result :
        idx = i+1
        result = distance[i]
        cnt = 1
    elif distance[i] == result:
        cnt+=1
        
print(idx, result, cnt)