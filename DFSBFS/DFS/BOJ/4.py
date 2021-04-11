#https://www.acmicpc.net/problem/1012
#백준 1012번 유기농 배추(BFS)
import sys
sys.setrecursionlimit(100000) #파이썬에서는 재귀 깊이 제한을 제거해야 한다

def dfs(x, y):
    check[x][y] = True
    for dx, dy in (-1,0), (1,0), (0,-1), (0,1):
        nx, ny = x+dx, y+dy
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if not check[nx][ny] and connect[nx][ny] == 1:
            dfs(nx, ny)

t = int(input())
for i in range(t):
    m, n, k = map(int, input().split())
    connect=[[0]*(m) for _ in range(n)]
    check = [[False]*(m) for _ in range(n)]
    count = 0
    
    for j in range(k):
        a,b=map(int,input().split())
        connect[b][a] = 1
    
    for r in range(n):
        for c in range(m):
            if not check[r][c] and connect[r][c] == 1:
                dfs(r,c)
                count+=1
    print(count)