#https://www.acmicpc.net/problem/16956
#백준 16956번 늑대와 양(BFS)
#import sys
#input = sys.stdin.readline
from collections import deque

r, c = map(int, input().split())
board = []
board_new = []
flag = True
direction = [(-1,0),(1,0),(0,1),(0,-1)]
check = set([])

for i in range(r):
    board.append(input())
    
for i in range(r):
    if not flag:
            break
    for j in range(c):
        if board[i][j] == 'W':
            for x,y in direction:
                dx=x+i
                dy=y+j
                if dx < 0 or dx >=r or dy < 0 or dy >=c or board[dx][dy] == 'W':
                    continue
                elif board[dx][dy] == 'S':
                    flag = False
                    break
                else:
                    check.add((dx,dy))
                    
if not flag:
    print(0)
else:
    print(1)
    for i in range(r):
        data = []
        for j in range(c):
            if (i,j) in check:
                data.append("D")
            else:
                data.append(board[i][j])
        board_new.append(data)
    for i in board_new:
        print("".join(i))
'''
파이썬에서 string은 변경이 안되서 값을 완전히 새로 넣어주는 방식으로 해결했는데
리스트의 요소로써 문자는 값을 변경할 수 있었다. 완전 비효율적으로 문제를 풀어서
시간 효율성 면에서 엄청 최악이었다.
'''