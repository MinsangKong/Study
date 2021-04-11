#https://www.acmicpc.net/problem/2667
#백준 2667번 단지번호붙히기(BFS)
#import sys
#input = sys.stdin.readline
from collections import deque

def bfs(x,y):
    q = deque()
    q.append((x,y))
    visited[x][y] = 1
    num = 1
    while q:
        dx, dy = q.popleft()
        for a,b in direction:
            nx = dx+a
            ny = dy+b
            if nx < 0 or nx >= n or ny < 0 or ny >= n :
                continue
            elif board[nx][ny] == '1' and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                num+=1
                q.append((nx,ny))
    result.append(num)
        

n = int(input())
board = []
for _ in range(n):
    board.append(list(input()))
    
result = []
direction = [(1,0),(-1,0),(0,1),(0,-1)]
visited = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if board[i][j] == '1' and visited[i][j] == 0:
            bfs(i,j)
            
result.sort()
print(len(result))
for i in result:
    print(i)