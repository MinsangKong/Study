#https://www.acmicpc.net/problem/1939
#백준 1939번 중량제한(이분탐색,BFS)
#import sys
#input = sys.stdin.readline
from collections import deque
def bfs(mid):
    q = deque()
    visited[fac1] = 1
    q.append(fac1)
    while q:
        x = q.popleft()
        if x == fac2:
            return True
        for y, cost in bridges[x]:
            if visited[y] == 0 and mid <= cost:
                q.append(y)
                visited[y] = 1
    return False
                
n, m = map(int, input().split())
bridges = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    bridges[a].append((b,c))
    bridges[b].append((a,c))
    
fac1, fac2 = map(int, input().split())
start = 1
end = 1000000000
result = 0
while start <= end:
    mid = (start+end)//2
    visited = [0]*(n+1)
    print(start, mid, end)
    if bfs(mid):
        result = mid
        start = mid+1
    else:
        end = mid-1
print(result)
'''
BFS가 떠올랐다면 쉬운 문제였지만 BFS가 바로 안 떠올라서 엄청 해맨 문제. 후... 정말
오래걸렸다...
'''