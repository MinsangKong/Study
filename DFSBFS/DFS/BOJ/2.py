#https://www.acmicpc.net/problem/2606
#백준 2606번 바이러스(DFS)
n=int(input())
m=int(input())
count =0
connect=[[0]*(n+1) for _ in range(n+1)]
visited=[False]*(n+1)
for i in range(m):
    a,b=map(int,input().split())
    connect[a][b]=1
    connect[b][a]=1
def dfs(v):
    visited[v]=True
    for i in range(1,n+1):
        if not visited[i] and connect[v][i]:
            global count
            count=count+1
            dfs(i)
dfs(1)
print(count)