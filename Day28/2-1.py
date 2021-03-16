#https://www.acmicpc.net/problem/2252
#백준 2252번 줄 세우기(그래프이론, 위상정렬)
#import sys
#input = sys.stdin.readline
from collections import deque

v, e = map(int, input().split())
indegree = [0] * (v + 1)
graph = [[] for i in range(v + 1)]

for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b) 
    indegree[b] += 1

def topology_sort():
    result = [] 
    q = deque() 

    for i in range(1, v + 1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        result.append(now)
        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)
    for i in result:
        print(i, end=' ')
topology_sort()

'''
아 맨 처음에 크루스컬로 해결할 수 있는 문제인 줄 알고 root 찾기로 풀고 있었는데
계속 답이 안나와서 구글링해보니까 애초에 위상정렬 문제였다. 위상정렬을 적용해서
바로 해결하긴 했지만 범위를 정해주지 않으면 적용할 알고리즘을 제대로 적용 못하는 걸
보면 아직 공부가 많이 필요하다...
'''