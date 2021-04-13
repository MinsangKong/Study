#https://www.acmicpc.net/problem/2206
#백준 2206번 벽 부수고 이동하기
#import sys
#input = sys.stdin.readline
from collections import deque

def bfs():
    q = deque()
    q.append((0,0,1))
    visited = [[[0]*2 for _ in range(m)] for _ in range(n)]
    visited[0][0][1] = 1
    while q:
        x,y,check = q.popleft()
        if x == n-1 and y == m-1:
            return visited[x][y][check]
        for a, b in direction:
            dx = x+a
            dy = y+b
            if dx < 0 or dx >= n or dy < 0 or dy >= m:
                continue
            elif board[dx][dy] == 1 and check == 1:
                visited[dx][dy][0] = visited[x][y][1]+1
                q.append((dx,dy,0))
            elif board[dx][dy] == 0 and visited[dx][dy][check] == 0:
                visited[dx][dy][check] = visited[x][y][check]+1
                q.append((dx,dy,check))
    return -1
                
n, m = map(int, input().split())
board = []
direction = [(1,0),(-1,0),(0,1),(0,-1)]
for i in range(n):
    board.append(list(map(int, input().strip())))
result = bfs()       
print(result)