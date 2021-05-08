from collections import deque
def bfs(x,y,place):
    q = deque()
    visited = [[0]*5 for _ in range(5)]
    visited[x][y] = 1
    direction = [(1,0),(-1,0),(0,1),(0,-1)]
    q.append((x,y,0))
    while q:
        a,b,dist = q.popleft() 
        for dx,dy in direction:
            nx = dx+a
            ny = dy+b
            if 0 <= nx < 5 and 0 <= ny < 5:
                if place[nx][ny] == 'P' and visited[nx][ny] == 0:
                    if dist < 2:
                        return False
                    else:
                        visited[nx][ny] = 1
                        q.append((nx,ny,dist+1))
                elif place[nx][ny] == 'O' and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    q.append((nx,ny,dist+1))
    return True
def solution(places):
    answer = []
    for place in places:
        flag = True
        for i in range(5):
            if not flag:
                break
            for j in range(5):
                if place[i][j] == 'P' :
                    if not bfs(i,j,place):
                        flag=False
                        break
        if flag:
            answer.append(1)
        else:
            answer.append(0)               
    return answer
print(solution([["POOOP", "XOXOP", "OOXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPXX", "OXXXP", "POOXX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))