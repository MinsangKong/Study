#Q41 여행 계획
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, input().split())
graph = []
parent = [i for i in range(n)]

for _ in range(n):
    graph.append(list(map(int, input().split())))
    
citys = list(map(int, input().split()))

for i in range(n):
    for j in range(i+1,n):
        if graph[i][j] == 1:
            union_parent(parent,i,j)
        
flag = True

for i in range(1,m):
    if find_parent(parent, citys[i-1]-1) != find_parent(parent, citys[i]-1):
        flag = False
        break
    
if flag:
    print("YES")
else:
    print("NO")