#https://www.acmicpc.net/problem/1956
#백준 1956번 운동(플로이드,다익스트라)
#import sys
#input = sys.stdin.readline
INF =int(1e9)

v,e = map(int,input().split())
graph =[[INF for _ in range(v)] for _ in range(v)]

for i in range(v):
    graph[i][i] = 0

for i in range(e):
    a,b,c = map(int,input().split())
    graph[a-1][b-1]=c

for k in range(v):
    for i in range(v):
        for j in range(v):
            graph[i][j] = min(graph[i][j],graph[i][k]+graph[k][j])

result=INF
for i in range(v-1):
    for j in range(i+1, v):
        result = min(result,graph[i][j]+graph[j][i])

if result ==INF:
    print(-1)
else:
    print(result)
'''
되돌아 온다는 개념을 잘 못 생각해서 오래 걸렸다...
플로이드로 감을 못잡아서 bfs로 풀었는데 바로 틀렸습니다가 나왔다. 차라리 다익스트라로
풀었으면 맞는 문제였다...
'''