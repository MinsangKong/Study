#https://www.acmicpc.net/problem/16236
#백준 16236번 아기상어(구현, bfs)
#import sys
#input=sys.stdin.readline
from collections import deque
def bfs(i, j):
    visited = [[0] * n for i in range(n)]
    visited[i][j] = 1
    fish = []
    dist = [[0] * n for i in range(n)]
    q = deque()
    q.append([i, j])
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
                if sea[nx][ny] <= sea[i][j] or sea[nx][ny] == 0:
                    q.append([nx, ny])
                    visited[nx][ny] = 1
                    dist[nx][ny] = dist[x][y] + 1
                if sea[nx][ny] < sea[i][j] and sea[nx][ny] != 0:
                    fish.append([nx, ny, dist[nx][ny]])
    if not fish:
        return -1, -1, -1
    #거리, y좌표, x좌표 순서로 정렬
    fish.sort(key = lambda x : (x[2], x[0], x[1]))
    return fish[0][0], fish[0][1], fish[0][2]
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
n = int(input())
sea = []
x, y = 0, 0
for i in range(n):
    a = list(map(int, input().split()))
    sea.append(a)
    for j in range(n):
        if a[j] == 9:
            sea[i][j] = 2
            x, y = i, j
eat_cnt = 0
cnt = 0
while True:
    i, j = x, y
    ex, ey, dist = bfs(i, j)
    if ex == -1: break
    sea[ex][ey] = sea[i][j]
    sea[i][j] = 0
    x, y = ex, ey
    eat_cnt += 1
    if eat_cnt == sea[ex][ey]:
        eat_cnt = 0
        sea[ex][ey] += 1
    cnt += dist
print(cnt)
'''
bfs로 먹이가 있는 곳 위치를 찾는 것까지는 이해 했는데 문제에서 요구하는 조건을 
어떻게 채워야 할 지 감이 안 잡혀서 해설을 봤다. lambda를 사용해서 거리,
y좌표, x좌표 순서로 정렬한 다음에 가장 앞에 있는 요소를 내보내면 답이 나왔다.
아직도 문제를 보면 bfs를 적용하는 것까지는 이해하는데 이를 구현과 합쳐지면
엄청 헤매고 있다....
'''