#https://www.acmicpc.net/problem/6497
#백준 6497번 전력난(MST, 크루스컬)
#import sys
#input = sys.stdin.readline
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
        heapq.heappush(edges, [c,a-1,b-1])
        
    cnt = 0
    result = 0
    while edges:
        cost, a, b = heapq.heappop(edges)
        if find_parent(parent,a) != find_parent(parent,b):
            union_parent(parent,a,b)
            result += cost
            cnt += 1
        if cnt == m-1:
            break
            
    print(total - result)