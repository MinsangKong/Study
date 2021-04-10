#https://www.acmicpc.net/problem/3055
#백준 3055번 탈출(BFS)
#import sys
#input = sys.stdin.readline
from collections import deque

def bfs(x,y,water):
    q = deque()
    q.append((x,y,0))
    num = 0
    global flag
    visited[x][y] = 1
    wq = deque()
    for i in water:
        wq.append(i)
    while q:
        dx, dy, cost = q.popleft()
        if cost > num and flag:
            num=cost
            arr = deque()
            while wq:
                wx, wy = wq.popleft()
                for a, b in direction:
                    nx = a+wx
                    ny = b+wy
                    if nx < 0 or nx >= r or ny < 0 or ny >= c:
                        continue
                    elif board[nx][ny] == '.':
                        arr.append((nx,ny))
                        board[nx][ny] = '*'
            wq = arr
        
        for a,b in direction:
            nx = a+dx
            ny = b+dy
            if nx < 0 or nx >= r or ny < 0 or ny >= c:
                continue
            elif board[dx][dy] == '*':
                continue
            elif board[nx][ny] == '*' or board[nx][ny]== 'X':
                continue
            elif board[nx][ny] == 'D':
                return cost+1
            elif board[nx][ny] == '.' and visited[nx][ny]==0:
                q.append((nx,ny,cost+1))
                visited[nx][ny] = 1
                
    return -1
            
r, c = map(int, input().split())

board = []
start = [0]*2
water = []
flag = False
visited =[[0]*c for _ in range(r)]

direction = [(1,0),(-1,0),(0,1),(0,-1)]
for i in range(r):
    data = list(input())
    for j in range(c):
        if data[j] == 'S':
            start[0], start[1] = i, j
        elif data[j] == '*':
            water.append((i,j))
            flag = True
    board.append(data)
    
result = bfs(start[0],start[1],water)

if result > 0:
    print(result)
else:
    print("KAKTUS")
    
'''
틀린 테스트 케이스를 못 찾아서 너무 오래 걸렸다. 다음에 문제 풀 때는 문제를 자세히
읽어야 겠다...
'''