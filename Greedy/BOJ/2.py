#https://www.acmicpc.net/problem/11779
#백준 11779번 최소비용 구하기2(그리디)
import heapq 
import sys 
input = sys.stdin.readline
INF = int(1e9)

n = int(input()) 
m = int(input()) 
graph = [[] for _ in range(n+1)] 
for _ in range(m):
    fr, to, cost = map(int, input().split()) 
    graph[fr].append((to,cost)) 
start, end = map(int, input().split()) 
distance = [INF for _ in range(n+1)] # 거리 
path = [-1 for _ in range(n+1)] # 최단 경로를 담을 배열 
q = [(0,start)] # 다익스트라를 쓸 우선순위 큐(비용, 노드) 
heapq.heapify(q) 
while q:
    now_cost, now = heapq.heappop(q) 
    if now_cost > distance[now]: 
        continue 
    if now == start:
        distance[now] = 0 
    for next_node, next_cost in graph[now]:
        path_cost = next_cost + now_cost 
        if path_cost < distance[next_node]: 
            distance[next_node] = path_cost 
            path[next_node] = now
            heapq.heappush(q, (path_cost, next_node)) # path가 갱신됐을 때 현재까지의 경로를 넣어준다. 
pathResult = [end]
temp = end
while path[temp] != -1:
    pathResult.append(path[temp])
    temp = path[temp]
print(distance[end]) 
print(len(pathResult))
for i in pathResult[::-1]:
    print(i, end=' ')