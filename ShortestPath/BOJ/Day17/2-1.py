#https://www.acmicpc.net/problem/18352 최단 경로
#백준 18352번 특정 거리의 도시 찾기
#다익스트라를 적용해서 풀어보니 계속 답이 틀려서 찾아보니 bfs로 해결 가능
#문제를 보고 어느 알고리즘을 적용해서 풀 수 있는가가 제일 어렵다
import sys
from collections import deque
input = sys.stdin.readline

n,m,k,x = map(int,input().split()) #도시 개수, 도로 개수, 거리 정보, 출발 도시 번호
#x에서 출발하여 거리가 k인 모든 도시를 찾아야 한다 
graph = [[] for _ in range(n+1)]
answer = [-1] * (n+1)
answer[x] = 0 
for _ in range(m):
    a, b = list(map(int,input().split()))
    graph[a].append(b)
que = deque([x])
while que:
    now = que.popleft()
    for nxt in graph[now]:
        if answer[nxt] == -1:
            answer[nxt] = answer[now] + 1 
            que.append(nxt) 
for i in range(n+1):
    if answer[i] == k:
        print(i)
if k not in answer:
    print(-1)