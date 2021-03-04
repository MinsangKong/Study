#https://www.acmicpc.net/problem/11779
#백준 11779번 최소비용 구하기2 (다익스트라)
import heapq 
#import sys 
#input = sys.stdin.readline
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
            path[next_node] = now #이전 node를 path 배열에 추가
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

'''
후 맨 처음에 플로이드로 풀었는데 문제가 도통 해결이 안되서 검색해보니 다익스트라로
푸는 문제였다. 아직도 문제를 보고 다익스트라로 풀어야 할지 플로이드로 풀어야 할지
감이 잘 잡히지 않는다. 최소가 되는 경로는 검색을 참고해서 만들었다.
맨 처음 생각한 방식은 path 배열을 2차원으로 만들어서 node마다 최소가 되는 경로를
계속 추가하는 방향으로 생각했는데 시간 초과가 발생할 것 같아서 해당 node의 이전 node를
입력해주고 역순으로 출력하는 방식으로 구현했다.
'''