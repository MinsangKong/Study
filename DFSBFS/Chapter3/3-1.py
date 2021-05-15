#Q17 경쟁적 전염
#import sys
#input = sys.stdin.readline
from collections import deque
def bfs(s):
    visited = [[0]*n for _ in range(n)]
    q = deque()
    for a in virus:
        q.append(a)
        visited[a[1]][a[2]] = 1
    while q:
        check, x, y, sec = q.popleft()
        if sec >= s:
            return
        for a,b in direction:
            dx = x+a
            dy = y+b
            if dx < 0 or dx >= n or dy < 0 or dy >= n:
                continue
            elif board[dx][dy] == 0:
                board[dx][dy] = check
                q.append([check, dx, dy, sec+1])
    return

n, k  = map(int, input().split())
board = []
virus = []

for _ in range(n):
    board.append(list(map(int, input().split())))
    
for i in range(n):
    for j in range(n):
        if board[i][j] != 0:
            virus.append([board[i][j],i,j,0])
virus.sort()
s, x, y = map(int, input().split())
direction = [(1,0),(-1,0),(0,1),(0,-1)]

bfs(s)

print(board[x-1][y-1])
'''
point는 deque는 sort함수를 제공하지 않기 때문에 virus 함수에서 sort를 해줘야 한다.
'''