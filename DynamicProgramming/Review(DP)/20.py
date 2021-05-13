#https://www.acmicpc.net/problem/1520
#백준 1520번 내리막길(DP,DFS)
import sys
#input = sys.stdin.readline
sys.setrecursionlimit(100000)

def dfs(x,y):
    if x == m-1 and y == n-1:
        return 1
    if dp[x][y] != -1:
        return dp[x][y]
    dp[x][y] = 0
    for a,b in direction:
        dx = x+a
        dy = y+b
        if 0 <= dx < m and 0 <= dy < n:
            if boards[dx][dy] < boards[x][y]:
                dp[x][y] += dfs(dx,dy)
    return dp[x][y]

m, n = map(int, input().split())
boards = []
direction = [(1,0),(-1,0),(0,1),(0,-1)]
for _ in range(m):
    boards.append(list(map(int, input().split())))
    
dp = [[-1]*n for _ in range(m)]
print(dfs(0,0))