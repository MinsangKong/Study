#https://www.acmicpc.net/problem/12761
#백준 12761번 돌다리(그래프이론)
from collections import deque
#import sys
#input = sys.stdin.readline
def bfs():
    while q:
        x = q.popleft()
        for i in range(8):
            if i < 6:
                nx = x + direction[i]
                if 0 <= nx <= 100000 and visited[nx] == 0:
                    q.append(nx)
                    visited[nx] = 1
                    bridge[nx] = bridge[x] + 1
            else:
                nx = x * direction[i]
                if 0 <= nx <= 100000 and visited[nx] == 0:
                    q.append(nx)
                    visited[nx] = 1
                    bridge[nx] = bridge[x] + 1
a, b, n, m = map(int, input().split())
bridge = [0 for i in range(100001)]
visited = [0 for i in range(100001)]
visited[n] = 1
direction = [1, -1, a, -a, b, -b, a, b]
q = deque()
q.append(n)
bfs()
print(bridge[m])