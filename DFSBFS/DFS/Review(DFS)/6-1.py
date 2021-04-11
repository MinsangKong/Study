#https://www.acmicpc.net/problem/2583
#백준 2583번 영역 구하기(DFS)
import sys
#input = sys.stdin.readline
sys.setrecursionlimit(3000000)

def dfs(x,y):
    stack = [(x,y)]
    board[x][y] = 1
    num = 1
    
    while stack:
        x, y = stack.pop()
        for dx, dy in direction:
            nx, ny = x+dx, y+dy
            if nx <0 or nx>= n or ny<0 or ny>=m:
                continue
            if board[nx][ny] == 0:
                stack.append((nx, ny))
                board[nx][ny] = 1
                num += 1
    result.append(num)
    
n, m, k = map(int, input().split())
board = [[0]*m for _ in range(n)]
direction = [(1,0),(-1,0),(0,1),(0,-1)]
result = []

for i in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for j in range(y1, y2):
        for k in range(x1, x2):
            board[j][k] = 1

for i in range(n):
    for j in range(m):
        if board[i][j] == 0:
            dfs(i,j)
print(len(result))
result.sort()
print(*result)
'''
거대한 수를 구하려고 할 때는 dfs, 그 반복 영역의 수를 구하려고 할 때는 bfs
명심하자
'''