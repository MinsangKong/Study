#https://www.acmicpc.net/problem/1707
#백준 1707번 이분그래프(BFS)
#import sys
#input = sys.stdin.readline
from collections import deque
def bfs(n):
    visited[n] = 1
    q = deque()
    q.append(n)
    while q:
        i = q.popleft()
        for j in arr[i]:
            if visited[j] == 0:
                visited[j]=-visited[i]
                q.append(j)
            else:
                if visited[j] == visited[i]:
                    return False
    return True
    
t = int(input())
for i in range(t):
    v, e = map(int, input().split())
    arr = [[] for _ in range(v)]
    flag = True
    visited = [0]*v
    for i in range(e):
        a, b = map(int, input().split())
        arr[a-1].append(b-1)
        arr[b-1].append(a-1)
    for i in range(v):
        if visited[i]==0:
            if not bfs(i):
                flag = False
                break
    print("YES" if flag else "NO")
                
    