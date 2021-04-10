#https://www.acmicpc.net/problem/5014
#백준 5014번 스타트링크(BFS)
#import sys
#input = sys.stdin.readline
from collections import deque
def bfs(n):
    q = deque()
    q.append((n,0))
    while q:
        i, cost = q.popleft()
        for j in direction:
            di = i+j
            if di < 0 or di >= f:
                continue
            elif di == g-1:
                return cost+1
            elif apt[di] > apt[i]+1:
                apt[di] = apt[i]+1
                q.append((di,cost+1))
    return -1
                
    
f, s, g, u, d = map(int, input().split())
#f : 총 층, g : 목표, s : 현재 위치, u : 위로 u층, d : 아래로 d층

apt = [int(1e9)]*f
apt[s-1] = 0
direction = [u,-d]
if s == g:
    print(0)
else:
    result = bfs(s-1)
    if result > 0:
        print(result)
    else:
        print("use the stairs")