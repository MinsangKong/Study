#https://www.acmicpc.net/problem/1937
#백준 1937번 욕심쟁이 판다(DP,DFS)
import sys
#input = sys.stdin.readline
sys.setrecursionlimit(100000)

def dfs(x, y):
    if dp[x][y] != -1:
        return dp[x][y]
    dp[x][y] = 1
    for a,b in direction:
        dx = x + a
        dy = y + b
        if 0 <= dx < n and 0 <= dy < n:
            if forest[dx][dy] > forest[x][y]:
                dp[x][y] = max(dp[x][y], dfs(dx, dy)+1)
    return dp[x][y]
    
n = int(input())
forest = []

for _ in range(n):
    forest.append(list(map(int, input().split())))
    
result = 0
direction = [(1,0),(-1,0),(0,1),(0,-1)]
dp = [[-1]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if dp[i][j] == -1:
            num = dfs(i,j)
            if num > result:
                result = num
            
print(result)
print(dp)