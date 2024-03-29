#https://www.acmicpc.net/problem/16236
#백준 16236번 아기상어(구현, bfs)
from heapq import heappop, heappush
import sys


def baby_shark():
    chk = [[False] * N for _ in range(N)]
    size, fish, cnt = 2, 0, 0
    while hq:
        dis, y, x = heappop(hq)
        if 0 < sea[y][x] < size:
            sea[y][x] = 0
            fish += 1
            cnt += dis
            dis = 0
            hq.clear()
            chk = [[False] * N for _ in range(N)]
            if size == fish:
                size += 1
                fish = 0

        for dx, dy in d:
            xi = x + dx
            yi = y + dy
            if 0 <= xi < N and 0 <= yi < N and not chk[yi][xi] and sea[yi][xi] <= size:
                chk[yi][xi] = True
                heappush(hq, (dis + 1, yi, xi))
    return cnt


d = [(0, -1), (1, 0), (0, 1), (-1, 0)]
N = int(input())
sea = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
hq = []
for i in range(N):
    if not hq:
        for j in range(N):
            if sea[i][j] == 9:
                heappush(hq, (0, i, j))
                sea[i][j] = 0
                break

result = baby_shark()
print(result)
'''
내가 작성한 코드는 324ms였는데 다른 사람이 작성한 코드는 빠르면 60ms선이었다.
왜 이렇게 차이가 많이 나는지 코드를 비교해 보니까 이 분은 bfs문에서 횟수 자체를 
계산해서 실행속도가 빠르고 나는 while문에서 bfs를 처리하고 정렬도 매번 해주었기 
때문에 실행속도가 차이 나는 것 같다...
'''