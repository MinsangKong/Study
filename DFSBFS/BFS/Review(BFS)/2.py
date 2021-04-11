#https://www.acmicpc.net/problem/10472
#백준 10472번 십자뒤집기(BFS)
#import sys
#input = sys.stdin.readline
from collections import deque
def bfs(a):
    queue = deque([(0,0)])
    while queue:
        c, v = queue.popleft()
        for i in range(9):
            tmp = 0
            for j in flip[i]:
                tmp += 1 << j
            nv = tmp ^ v
            if nv not in visited:
                queue.append((c+1,nv))
                visited[nv] = min(c + 1, visited.get(nv,512))
                if nv == a:
                    return visited[nv]


flip = {0:{0,1,3}, 1:{0,1,2,4},2:{1,2,5},3:{0,3,4,6},4:{1,3,4,5,7},5:{2,4,5,8},6:{3,6,7},7:{4,6,7,8},8:{5,7,8}}
T = int(input())
for t in range(T):
    board = ''
    for i in range(3):
        board += input().replace('*','1').replace('.','0')
    board = int(board, base=2)
    visited = {0: 0}
    if board == 0:
        print(0)
    else:
        print(bfs(board))
        