import sys
M,N,K = map(int, sys.stdin.readline().split())
g = [[0]*M for _ in range(N)]
for _ in range(K):
    frmx, frmy, tox, toy = map(int, sys.stdin.readline().split())

    for x in range(frmx, tox):
        for y in range(frmy, toy):
            g[x][y] = 1

land = []

def dfs(x,y):
    count = 1
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]

    g[x][y] = 1
    stack = [(x,y)]

    while stack:
        x,y = stack.pop()
        for i in range(4):
            nxtx = x+dx[i]
            nxty = y+dy[i]

            if 0<=nxtx<N and 0<=nxty<M and g[nxtx][nxty] == 0:
                g[nxtx][nxty] = 1
                stack.append((nxtx, nxty))
                count += 1

    land.append(count)

for i in range(N):
    for j in range(M):
        if g[i][j] == 0:
            dfs(i,j)

land.sort()
print(len(land))
print(" ".join(str(x) for x in land))
'''
비슷한 코드인데 속도는 20ms 정도 차이가 났다. why???
'''