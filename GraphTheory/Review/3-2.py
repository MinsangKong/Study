import heapq

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

while True:
    m, n = map(int, input().split())
    if m == 0 and n == 0:
        break
    parent = [i for i in range(m)]
    
    edges = []
    total = 0
    
    for _ in range(n):
        a,b,c = map(int, input().split())
        total += c
        edges.append([c,a-1,b-1])
        
    result = 0
    edges.sort()
    for edge in edges:
        cost, a, b = edge
        if find_parent(parent,a) != find_parent(parent,b):
            union_parent(parent,a,b)
            result += cost
            
    print(total - result)
'''
??? heapq를 쓸 때보다 정렬 할 때가 더 빨랐다. 문제마다 결과가 다르다...
'''