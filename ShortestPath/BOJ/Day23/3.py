#https://www.acmicpc.net/problem/14588
#백준 14588번 Line Friends(Small) (플로이드)
import sys
#input = sys.stdin.readline
INF = int(1e9)

n = int(input())
graph = []
for i in range(n):
    a, b = map(int,input().split())
    graph.append((a,b))
cost = [[INF]*n for i in range(n)]
result = []
for i in range(n):
    for j in range(n):
        if i == j:
            cost[i][j] = 0
            continue
        ai, bi = graph[i][0], graph[i][1]
        aj, bj = graph[j][0], graph[j][1]
        if max(ai,aj) <= min(bi,bj):
            cost[i][j] = 1 #거리가 1인 친구부터 구하기(선분이 겹치는)
for k in range(n):
    for i in range(n):
        for j in range(n):
            cost[i][j]=min(cost[i][j], cost[i][k]+cost[k][j]) 

m = int(input())
for i in range(m):
    a, b = map(int,input().split())
    dist = cost[a-1][b-1]
    if dist != INF:
        print(dist)
    else:
        print(-1)
'''
시간 초과 발생. for문을 여러 번 돌려서 그런것 같음.
pypy3로 제출하면 이상 없이 정답 뜸.(알고리즘 자체는 맞음)
선분이 겹치는 개념을 어떻게 구현할 지 모르겠어서 구글링 후 해석 참고,
알고리즘 자체는 어렵지 않았는데, 직관적으로 이렇게 해야겠다는 떠오르지 않아서
시간이 오래 걸렸음... 최단 경로 쪽은 해설 없이 완전히 혼자 푼게 몇 개 없다...
'''