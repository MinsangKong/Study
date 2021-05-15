#Q20 감시 피하기
#import sys
#input = sys.stdin.readline
from collections import deque
import copy
from itertools import combinations
def check(x, y, board, flag):
    for a,b in direction:
        dx = x+a
        dy = y+b
        while 0 <=dx < n and 0 <= dy < n:
            if board[dx][dy] == 'X':
                dx = dx + a
                dy = dy + b
                continue
            elif board[dx][dy] == 'O' or board[dx][dy] == 'T':
                break
            elif board[dx][dy] == 'S':
                flag = True
                return flag
    return flag

    
n = int(input())
school = []
direction = [(1,0),(-1,0),(0,1),(0,-1)]
teacher = []
cases = []

for _ in range(n):
    school.append(list(input().split()))
    
for i in range(n):
    for j in range(n):
        if school[i][j] == 'T':
            teacher.append((i,j))
        elif school[i][j] == 'X':
            cases.append((i,j))
            
caselist = list(combinations(cases, 3))

for case in caselist:
    board = copy.deepcopy(school)
    for x,y in case:
        board[x][y] = 'O'
    flag = False
    for x,y in teacher:
        flag = check(x,y,board,flag)
        if flag:
            break
    if not flag:
        print("YES")
        exit()

print("NO")
'''
중간에 생각이 꼬여서 엄청 오래 걸렸다... 후 생각이 한번 꼬이면 엄청 해메다가 푸는
것 같다...
'''