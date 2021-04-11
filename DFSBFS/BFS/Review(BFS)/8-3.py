#import sys
#input = sys.stdin.readline
def BFS():
    while q:
        x, y, w = q.pop(0)
        for dx, dy in ((0, -1), (0, 1), (-1, 0), (1, 0)):
            nx, ny = x + dx, y + dy
            if nx < 0 or ny < 0 or nx >= R or ny >= C: continue
            if maps[nx][ny] == 'D':
                if w: continue
                return dist[x][y]
            if dist[nx][ny] or maps[nx][ny] == 'X': continue
            dist[nx][ny] = dist[x][y] + 1
            q.append((nx, ny, w))
    return "KAKTUS"

R, C = map(int, input().split())
maps = [list(input()) for _ in range(R)]
q = []
dist = [[0] * C for _ in range(R)]
for x in range(R):
    for y in range(C):
        if maps[x][y] == 'S':
            sx, sy = x, y
            dist[x][y] = 1
        if maps[x][y] == '*':
            q.append((x, y, 1))
            dist[x][y] = 1
q.append((sx, sy, 0))
print(BFS())

'''
if dist[nx][ny] or map[nx][ny] == 'X': continue 이 구문을 통해서
물이 방문한 nx, ny는 dist 값이 존재하기 때문에 방문할 수 가 없다.
후 굳이 2가지를 하는 것보다 한 번에 처리하는 방식을 배워야 한다.
'''