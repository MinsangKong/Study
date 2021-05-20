from collections import deque
def bfs(v):
    q.append(v)
    c=[-1 for _ in range(n)]
    c[v]=0
    while q:
        v=q.popleft()
        for i in a[v]:
            if c[i]==-1:
                c[i]=c[v]+1
                q.append(i)
    cnt=0
    for i in range(n):
        if c[i]!=-1:
            cnt+=c[i]
    return cnt


n,m=map(int,input().split())
a=[[]for _ in range(n)]
q,res,ans=deque(),[],[]
for _ in range(m):
    x,y=map(int,input().split())
    x-=1
    y-=1
    a[x].append(y)
    a[y].append(x)
for i in range(n):
    res.append(bfs(i))

for i in range(n):
    if res[i]==min(res):
        ans.append(i)
print(min(ans)+1)