#https://www.acmicpc.net/problem/14716
#백준 14716번 현수막(DFS)
import sys
#input = sys.stdin.readline
sys.setrecursionlimit(3000000)

M,N=map(int,input().split())

table=[]
isvisited=[[False]*N for i in range(M)]
count=0

def bfs(i,j):
    if isvisited[i][j] or table[i][j]==0:
        return
    isvisited[i][j]=True
    if i>0:
        bfs(i-1,j)
        if j>0:
            bfs(i-1,j-1)
        if j<N-1:
            bfs(i-1,j+1)
    if i<M-1:
        bfs(i+1,j)
        if j>0:
            bfs(i+1,j-1)
        if j<N-1:
            bfs(i+1,j+1)
    if j > 0:
        bfs(i, j - 1)
    if j<N-1:
        bfs(i,j+1)
    return

for i in range(M):
    table.append(list(map(int,input().split())))

for i in range(M):
    for j in range(N):
        if not isvisited[i][j] and table[i][j]==1:
            count+=1
            bfs(i,j)
print(count)
'''
가장 빠르게 작성한 코드를 보니까 dfs를 실행할 때 애초에 조건을 만족하지 못하면
return하는 식으로 작성하면 40ms 정도 빨랐다.
'''