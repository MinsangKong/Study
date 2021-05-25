from collections import deque
import sys
input = sys.stdin.readline

def find(x):
    if p[x] == x:
        return x
    else:
        p[x] = find(p[x])
        return p[x]

def union(x, y):
    a = find(x)
    b = find(y)
    if a != b:
        p[b] = a

n, m, k = map(int, input().split())
graph = deque()
for i in range(1, m + 1):
    a, b = map(int, input().split())
    graph.append([a, b, i])

for _ in range(k):
    p = [i for i in range(n+1)]
    cnt = 0
    ans = 0
    for a, b, c in graph:
        if find(a) != find(b):
            union(a, b)
            ans += c
            cnt += 1
        if cnt == n - 1:
            break
    if cnt == n - 1:
        print(ans, end = ' ')
    else:
        print(0, end = ' ')
    graph.popleft()