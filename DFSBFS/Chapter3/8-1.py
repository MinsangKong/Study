#Q22 블록 이동하기
from collections import deque
def bfs(start,board):
    q = deque()
    q.append((start,0))
    visited = set()
    while q:
        pos, dist = q.popleft()
        visited.add(tuple(pos))
        l, r = pos[0],pos[1]
        if r[0] == len(board)-1 and r[1] == len(board)-1:
            return dist
        #로봇이 가로로 있는 경우
        if l[0] == r[0]:
            #왼쪽으로 이동
            new_pos = ((l[0],l[1]-1), (l[0],l[1]))
            #왼쪽으로 1 이동한 좌표가 아직 방문 한 좌표가 아니고 해당 좌표가 board 안에 있는 경우
            if 0<= new_pos[0][1] < len(board) and new_pos not in visited and board[new_pos[0][0]][new_pos[0][1]] == 0:
                visited.add(new_pos)
                q.append((new_pos, dist+1))
            #오른쪽으로 이동
            new_pos = ((r[0],r[1]), (r[0],r[1]+1))
            #오른쪽으로 1 이동한 좌표가 아직 방문 한 좌표가 아니고 해당 좌표가 board 안에 있는 경우
            if  0 <= new_pos[1][1] < len(board) and new_pos not in visited and board[new_pos[1][0]][new_pos[1][1]] == 0:
                visited.add(new_pos)
                q.append((new_pos,dist+1))
            #상하 이동
            for dy in [-1,1]:
                new_pos = ((l[0]+dy,l[1]), (r[0]+dy, r[1]))
                if 0 <= new_pos[0][0] < len(board) and new_pos not in visited and board[new_pos[0][0]][new_pos[0][1]] == board[new_pos[1][0]][new_pos[1][1]] == 0:
                    visited.add(new_pos)
                    q.append((new_pos,dist+1))
            
            #회전
            for dy in [-1,1]:
                #왼쪽 좌표를 기준으로 회전
                #오른쪽 좌표의 위, 아래 좌료가 board 범위 내에 있고 값이 0인 경우 회전이 가능
                if 0 <= r[0]+dy < len(board) and board[r[0]+dy][r[1]] == 0:
                    new_r = (l[0]+dy, l[1])
                    new_pos = tuple(sorted([l,new_r], key = lambda x : (x[0],x[1])))
                    if 0 <= new_r[0] < len(board) and board[new_r[0]][new_r[1]] == 0 and new_pos not in visited:
                        visited.add(new_pos)
                        q.append((new_pos, dist+1))
        
                #오른쪽 좌표 기준 회전
                #왼쪽 좌표의 위, 아래 좌료가 board 범위 내에 있고 값이 0인 경우 회전이 가능(대각선 좌표)
                if 0 <= l[0]+dy < len(board) and board[l[0]+dy][l[1]] == 0:
                    new_l = (r[0]+dy, r[1])
                    new_pos = tuple(sorted([new_l, r], key = lambda x : (x[0],x[1])))
                    if 0 <= new_l[0] < len(board) and board[new_l[0]][new_l[1]] == 0 and new_pos not in visited:
                        visited.add(new_pos)
                        q.append((new_pos, dist+1))
        
        #로봇이 세로로 있는 경우
        if l[1] == r[1]:
            #위로 이동
            new_pos = ((l[0]-1, l[1]), (l[0],l[1]))
            if 0 <= new_pos[0][0] < len(board) and new_pos not in visited and board[new_pos[0][0]][new_pos[0][1]] == 0:
                visited.add(new_pos)
                q.append((new_pos, dist+1))
            #아래로 이동
            new_pos = ((r[0],r[1]),(r[0]+1, r[1]))
            if 0 <= new_pos[1][0] < len(board) and new_pos not in visited and board[new_pos[1][0]][new_pos[1][1]] == 0 :
                visited.add(new_pos)
                q.append((new_pos,dist+1))
            #좌우로 이동
            for dx in [-1,1]:
                new_pos = ((l[0],l[1]+dx), (r[0],r[1]+dx))
                if 0 <= new_pos[0][1] < len(board) and new_pos not in visited and board[new_pos[0][0]][new_pos[0][1]] == board[new_pos[1][0]][new_pos[1][1]] == 0:
                    visited.add(new_pos)
                    q.append((new_pos, dist+1))
            
            #회전
            for dx in [-1,1]:
                #위쪽(l) 기준으로 회전
                #아래쪽(r) 값의 좌/우 좌표가 board 범위 내에 있고, 값이 0인 경우 회전 가능
                if 0 <= r[1]+dx < len(board) and board[r[0]][r[1]+dx] == 0:
                    new_r = (l[0],l[1]+dx)
                    new_pos = tuple(sorted([l,new_r], key = lambda x : (x[0],x[1])))
                    if 0 <= new_r[0] < len(board) and board[new_r[0]][new_r[1]] == 0 and new_pos not in visited:
                        visited.add(new_pos)
                        q.append((new_pos,dist+1))
                #아래쪽 좌표 기준 회전
                #위쪽 값의 좌/우 좌료가 board 범위 내에 있고, 값이 0일 경우 
                if 0 <= l[1]+dx < len(board) and board[l[0]][l[1]+dx] == 0:
                    new_l = (r[0],r[1]+dx)
                    new_pos = tuple(sorted([new_l, r], key = lambda x : (x[0],x[1])))
                    if 0 <= new_l[0] < len(board) and board[new_l[0]][new_l[1]] == 0 and new_pos not in visited:
                        visited.add(new_pos)
                        q.append((new_pos,dist+1))
                        
def solution(board):
    return bfs(((0,0),(0,1)), board)
'''
정말 어려웠던 문제. 회전 함수의 구현과 방문 여부를 체크하는게 어려웠다. 
항상 방문 여부는 list로 체크하다보니 set에 add하는 방식은 떠오르지 못했다...
그리고 회전하는 경우 l,r가 바뀔 수 있기 때문에 sort하는 것이 필요하다.
회전 함수의 포인트는 회전하는 축을 지정한 다음에 경우의 수를 구현하는 게 포인트였다.
특별히 어려운 문법은 없었지만 시험장에서 문제를 푼다면 조건이 많아서 시간이 오래 걸릴 것 같다.
아 그리고 파이썬에서 set은 {(1, 1), (1, 2)}와 {(1, 2), (1, 1)}을 같은 집합 객체로 본다.
'''