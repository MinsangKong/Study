#Q39 화성 탐사
import heapq
INF = int(1e9)

def dijkstra(x,y):
    distance = [[INF]*n for _ in range(n)]
    distance[x][y] = graph[x][y]
    q = []
    heapq.heappush(q, (distance[x][y],x,y))
    direction = [(1,0),(-1,0),(0,1),(0,-1)]
    while q:
        dist, dx, dy = heapq.heappop(q)
        if dx == n-1 and dy == n-1:
            print(distance)
            return distance[n-1][n-1]
        
        if dist > distance[dx][dy]:
            continue
            
        for a,b in direction:
            nx = dx+a
            ny = dy+b
            if 0 <= nx < n and 0 <= ny < n:
                cost = dist+graph[nx][ny]
                if cost < distance[nx][ny]:
                    distance[nx][ny] = cost
                    heapq.heappush(q,(cost,nx,ny))

t = int(input())


for _ in range(t):
    n = int(input())
    graph = []
    
    for _ in range(n):
        graph.append(list(map(int, input().split())))
    
    print(dijkstra(0,0))