#https://www.acmicpc.net/problem/9470
#백준 9470번 Strahler 순서(위상정렬)
#import sys
#input = sys.stdin.readline
from collections import deque

t = int(input())

for _ in range(t):
    k,m,p = map(int, input().split())
    graph = [[] for _ in range(m)]
    check = [[] for _ in range(m)]
    indegree = [0]*m
    
    for _ in range(p):
        a, b = map(int, input().split())
        graph[a-1].append(b-1)
        check[b-1].append(a-1)
        indegree[b-1]+=1
        
    q = deque()
    result = [0]*m
    
    for i in range(m):
        if indegree[i] == 0:
            q.append(i)
            result[i]=1
            
    while q:
        now = q.popleft()
        
        for i in graph[now]:
            indegree[i]-=1
            
            if indegree[i] == 0:
                q.append(i)
        
        cnt = 0
        cost = 0
        for i in check[now]:
            if cost < result[i]:
                cost = result[i]
                cnt = 1
            elif cost == result[i]:
                cnt+=1
                
        if cost > 0:
            if cnt >= 2:
                result[now] = cost+1
            else:
                result[now] = cost
    
    print(k, result[m-1])