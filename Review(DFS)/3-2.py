#https://www.acmicpc.net/problem/1325
#백준 1325번 효율적인 해킹(BFS)
#import sys
#input = sys.stdin.readline
from collections import deque

def bfs(i):
    q = deque()
    q.append(i)
    cnt = 1
    visited = [0] * n
    visited[i] = 1
    while q :
        num = q.popleft()
        for j in arr[num]:
            if visited[j] == 0 :
                visited[j] == 1
                q.append(j)
                cnt+=1
    result.append(cnt)

n, m = map(int, input().split())
arr = [[] for _ in range(n)]

result = []

for i in range(m):
    a, b = map(int, input().split())
    arr[b-1].append(a-1)

for i in range(n):
    bfs(i)

for i in range(n):
    if result[i] == max(result):
        print(i+1, end=' ')