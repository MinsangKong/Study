#https://www.acmicpc.net/problem/1005
#백준 1005번 ACM Craft(위상정렬)
#import sys
#input = sys.stdin.readline
from collections import deque
import copy

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    times = list(map(int, input().split()))
    indegree = [0]*n
    
    graph = [[] for _ in range(n)]
    
    for _ in range(k):
        a, b = map(int, input().split())
        graph[a-1].append(b-1)
        indegree[b-1]+=1
        
    target = int(input())
    q = deque()
    
    for i in range(n):
        if indegree[i] == 0:
            q.append(i)
            
    result = copy.deepcopy(times)
    while q :
        now = q.popleft()
        
        check = 0
        for i in graph[now]:
            indegree[i] -= 1
            result[i] = max(result[i], result[now]+times[i])
            if indegree[i] == 0 :
                q.append(i)
    
    print(result[target-1])