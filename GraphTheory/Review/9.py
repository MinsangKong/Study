#https://www.acmicpc.net/problem/14950
#백준 14950번 정복자(MST,크루스컬)
#import sys
#input = sys.stdin.readline
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a > b :
        parent[a] = b
    else:
        parent[b] = a

n, m, t = map(int, input().split())
graph = []
parent = [i for i in range(n)]

for _ in range(m):
    a,b,c = map(int, input().split())
    graph.append([c,a-1,b-1])
    
graph.sort()

result = 0
cnt = 0
for i in graph:
    cost, a, b = i
    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent, a, b)
        result += cost + t*cnt
        cnt+=1
    if cnt == n-1:
        break
        
print(result)