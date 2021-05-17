#https://www.acmicpc.net/problem/1446
#백준 1446번 지름길(다익스트라, DP)
#import sys
#input = sys.stdin.readline

n, d = map(int, input().split())
graph = []
distance = [i for i in range(d+1)]

for _ in range(n):
    a,b,c = map(int, input().split())
    graph.append([a,b,c])
for i in range(d+1):
    if i > 0:
        distance[i] = min(distance[i],distance[i-1]+1)
    for start,end,cost in graph:
        if start == i and end <= d and cost < distance[end]-distance[start] :
            distance[end] = cost+distance[start]
print(distance[d])
        