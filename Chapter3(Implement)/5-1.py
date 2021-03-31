#11 뱀
#import sys
#input = sys.stdin.readline
from collections import deque

#뱀의 회전
def rotate(direction, cha):
    if cha == "L":
        direction = (direction - 1) % 4
    else:
        direction = (direction + 1) % 4
    return direction
        
#몸에 닿는지 여부 체크
def check(x,y): 
    if [x,y] in q:
        return False
    return True

n = int(input())
board = [[0] * (n+1) for _ in range(n+1)]
k = int(input())
for i in range(k):
    x, y = map(int, input().split())
    board[x][y] = 1
    
l = int(input())
directions = deque()
for i in range(l):
    a, b = input().split()
    directions.append([int(a), b])
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
direction = 0
q = deque()
q.append([1,1])
count = 0
while True:
    x, y = q[-1][0], q[-1][1] #뱀의 머리부분
    x += dx[direction]
    y += dy[direction]
    if 0 < x <= n and 0 < y <= n:
        if not check(x,y):
            break
        q.append([x,y])
        if board[x][y] == 1:
            board[x][y] = 0
        else:
            q.popleft()
    else:
        break
    count+=1
    if directions and count == directions[0][0]:
        direction = rotate(direction, directions[0][1])
        directions.popleft()

print(count+1)
'''
아 바보처럼 board[x][y] = 0을 board[x][y] == 0 이라고 해서 백준에서 문제를 풀 때
계속 오류가 발생했다. 허망하다.
'''