#https://www.acmicpc.net/problem/1197
#백준 1197번 최소 스패닝트리(MST,크루스컬)
#import sys
#input = sys.stdin.readline
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

v, e = map(int, input().split())
parent = [0] * v 

edges = []
result = 0

for i in range(v):
    parent[i] = i
    
for _ in range(e):
    a,b,c = map(int, input().split())
    edges.append([c,a-1,b-1])
    
edges.sort()

for edge in edges:
    cost, a, b = edge
    
    if find_parent(parent,a) != find_parent(parent, b):
        union_parent(parent,a,b)
        result += cost
        
print(result)