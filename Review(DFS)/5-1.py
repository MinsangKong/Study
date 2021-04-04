#https://www.acmicpc.net/problem/14716
#백준 14716번 현수막(DFS)
import sys
#input = sys.stdin.readline
sys.setrecursionlimit(3000000)

def dfs(x,y):
    visited[x][y] = 1
    for a,b in direction:
        dx = x+a
        dy = y+b
        if dx < 0 or dx >= m or dy < 0 or dy >= n:
            continue
        elif visited[dx][dy] == 0 and banner[dx][dy] == 1:
            dfs(dx, dy)
            
    
m, n = map(int, input().split())
banner = []
visited = [[0]*n for _ in range(m)]
direction = [(1,0), (-1,0), (0,1), (0,-1), (1,1), (-1,1), (1,-1), (-1,-1)]
cnt = 0

for i in range(m):
    banner.append(list(map(int, input().split())))
    
for i in range(m):
    for j in range(n):
        if visited[i][j] == 0 and banner[i][j] == 1:
            dfs(i,j)
            cnt+=1
            
print(cnt)
'''
중간에 dy = y+b를 dy=x+b로 작성해서 시간만 잡아 먹었다.ㅡㅡ 실수 하나가 때문에
시간만 오래 잡아 먹었다.
'''