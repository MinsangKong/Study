#Q45 최종 순위
#https://www.acmicpc.net/problem/3665
#import sys
#input = sys.stdin.readline
from collections import deque

t = int(input())

for _ in range(t):
    n = int(input())
    lastScore = list(map(int, input().split()))
    check = [[0]*n for _ in range(n)]
    indegree = [0]*n
    
    for i in range(n):
        for j in range(i+1,n):
            check[lastScore[j]-1][lastScore[i]-1] = 1
            indegree[lastScore[i]-1] += 1
            
    m = int(input())
    
    for _ in range(m):
        a, b = map(int, input().split())
        if not check[a-1][b-1]:
            a,b = b,a
        check[a-1][b-1],check[b-1][a-1] = 0, 1
        indegree[a-1] += 1
        indegree[b-1] -= 1
        
    q = deque()
    result = []
    cnt = 0
    
    for i in range(n):
        if indegree[i] == 0:
            cnt += 1
            q.append(i)
            
    if cnt != 1:
        if cnt > 1:
            print("?")
        elif cnt == 0:
            print("IMPOSSIBLE")
        continue
        
    while q and cnt == 1:
        cnt = 0
        now = q.popleft()
        result.append(now+1)
        for i in range(n):
            if check[now][i]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    cnt += 1
                    q.append(i)
                    
    if cnt > 1:
        print("?")
    elif len(result) != n:
        print("IMPOSSIBLE")
    else:
        print(*result[::-1])