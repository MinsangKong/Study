#https://www.acmicpc.net/problem/3184
#백준 3184번 양(BFS)
#import sys
#input = sys.stdin.readline
from collections import deque
def bfs(x,y):
    q = deque()
    q.append((x,y))
    visited[x][y] = 1
    sheep = 0
    wolf = 0
    if board[x][y] == "o":
        sheep+=1
    elif board[x][y] == "v":
        wolf+=1
    while q:
        dx, dy = q.popleft()
        for a, b in direction:
            nx = a+dx
            ny = b+dy
            if nx < 0 or nx >= r or ny < 0 or ny >= c:
                continue
            elif board[nx][ny] == "#":
                continue
            elif board[nx][ny] == "o" and visited[nx][ny] == 0:
                sheep+=1
                q.append((nx,ny))
                visited[nx][ny] = 1
            elif board[nx][ny] == "v" and visited[nx][ny] == 0:
                wolf+=1
                q.append((nx,ny))
                visited[nx][ny] = 1
            elif board[nx][ny] == "." and visited[nx][ny] == 0:
                q.append((nx,ny))
                visited[nx][ny]=1
    
    if sheep > wolf:
        result[0]+=sheep
    else :
        result[1]+=wolf

r, c = map(int, input().split())
board = []
for i in range(r):
    board.append(list(input()))
    
result = [0]*2
direction = [(1,0),(-1,0),(0,1),(0,-1)]
visited = [[0]*c for _ in range(r)]
    
for i in range(r):
    for j in range(c):
        if visited[i][j] == 0 and board[i][j] != "#":
            bfs(i,j)
            
print(*result)

'''
여기서도 visited 배열을 별개로 만들지 않고 board 배열에 방문한 값을 "#"으로 바꿔
줬으면 시간효율성 면에서 훨씬 좋았을 것 같다.
'''