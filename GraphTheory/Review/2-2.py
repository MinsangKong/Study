#https://www.acmicpc.net/problem/1922
#백준 1922번 네트워크 연결(MST, 크루스컬)
#import sys
#input = sys.stdin.readline
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a > b :
        parent[a] = b
    else:
        parent[b] = a
        
n = int(input())
m = int(input())

parent = [0]*n

for i in range(n):
    parent[i] = i
    
edges = []

for _ in range(m):
    a,b,c = map(int, input().split())
    edges.append([c,a-1,b-1])
    
edges.sort()

result = 0

for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent,b):
        union_parent(parent, a, b)
        result+= cost
        
print(result)