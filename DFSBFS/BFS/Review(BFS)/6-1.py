#https://www.acmicpc.net/problem/2178
#백준 2178번 미로탐색(BFS)
#import sys
#input = sys.stdin.readline
from collections import deque

def bfs(x,y):
    q = deque()
    q.append((x,y))
    result[x][y] = 1
    while q:
        dx, dy = q.popleft()
        for a, b in direction:
            nx = a+dx
            ny = b+dy
            if nx < 0 or nx >=n or ny < 0 or ny >=m:
                continue
            elif maze[nx][ny] == "1" and result[nx][ny] > result[dx][dy]+1:
                result[nx][ny] = result[dx][dy]+1
                if nx == n-1 and ny == m-1:
                    return
                q.append((nx,ny))
    return
        

n, m = map(int, input().split())
maze = []
for _ in range(n):
    maze.append(list(input()))
    
result = [[int(1e9)]*m for _ in range(n)]
direction = [(1,0),(-1,0),(0,1),(0,-1)]

bfs(0,0)

print(result[n-1][m-1])
'''
여기서도 시간 효율성을 높이기 위해서는 result배열을 만들지 말고 q의 요소를
(x,y,cost)하는 식으로 하는게 좋을거 같다.
'''