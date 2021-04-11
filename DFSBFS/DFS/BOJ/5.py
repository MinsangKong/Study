#https://www.acmicpc.net/problem/11123
#백준 11123번 양 한마리... 양 두마리(DFS)
import sys
sys.setrecursionlimit(100000)

def dfs(x, y):
    check[x][y] = True
    for dx, dy in (-1,0), (1,0), (0,-1), (0,1):
        nx, ny = x+dx, y+dy
        if nx < 0 or nx >= h or ny < 0 or ny >= w:
            continue
        if not check[nx][ny] and a[nx][ny] == '#':
            dfs(nx, ny)

n = int(input())
for k in range(n):
    ans = 0
    h, w = map(int, input().split())
    a = [list(input().strip()) for _ in range(h)]
    check = [[False]*w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if not check[i][j] and a[i][j] == '#':
                dfs(i, j)
                ans += 1
    print(ans)
