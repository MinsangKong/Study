from itertools import combinations
from collections import deque
import copy

N,M = map(int, input().split())
lab, exlab, virus, space = [],[],[],[]
result = 0

dy = [-1,0,1,0]
dx = [0,1,0,-1]

for _ in range(N):
    lab.append(list(map(int, input().split())))

for i in range(N):
    for j in range(M):
        if lab[i][j] == 2:
            virus.append((i,j))
        if lab[i][j] == 0:
            space.append((i,j))

def VirusSpread():
    global exlab, N, M, virus
    q = deque()

    for pos in virus:
        q.append(pos)

    while q:
        cury, curx = q.popleft()
        for dir in range(4):
            ny = cury + dy[dir]
            nx = curx + dx[dir]

            if 0 <= ny < N and 0 <= nx < M and exlab[ny][nx] == 0:
                exlab[ny][nx] = 2
                q.append((ny,nx))

def SpaceCnt():
    global exlab, N, M

    cnt = 0
    for i in range(N):
        for j in range(M):
            if exlab[i][j] == 0:
                cnt += 1
    
    return cnt

for walls in list(combinations(space, 3)):
    
    exlab = copy.deepcopy(lab)
    for wall in walls:
        y, x = wall
        exlab[y][x] = 1
    
    VirusSpread()
    result = max(result, SpaceCnt())

print(result)