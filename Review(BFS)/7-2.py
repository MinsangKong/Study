#import sys
#input = sys.stdin.readline
from collections import deque

def bfs(x,y):
    q = deque()
    q.append((x,y))
    board[x][y] = '0'
    num = 1
    while q:
        dx, dy = q.popleft()
        for a,b in direction:
            nx = dx+a
            ny = dy+b
            if nx < 0 or nx >= n or ny < 0 or ny >= n :
                continue
            elif board[nx][ny] == '1' :
                board[nx][ny] = '0'
                num+=1
                q.append((nx,ny))
    result.append(num)
        

n = int(input())
board = []
for _ in range(n):
    board.append(list(input()))
    
result = []
direction = [(1,0),(-1,0),(0,1),(0,-1)]

for i in range(n):
    for j in range(n):
        if board[i][j] == '1':
            bfs(i,j)
            
result.sort()
print(len(result))
for i in result:
    print(i)
    
'''
의외로 visited 배열을 만든 경우와 시간은 88ms로 같았다. 기본적인 알고리즘이 비슷한데
그럼 다른 사람과의 코드와 왜 시간효율성 차이가 많이 나는지 잘 모르겠다...
'''