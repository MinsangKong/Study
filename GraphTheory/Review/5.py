#https://www.acmicpc.net/problem/13905
#백준 13905번 세부(MST, 크루스컬)
#import sys
#input = sys.stdin.readline
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
s, e = map(int, input().split())
parent = [i for i in range(n)]

graph = []

for _ in range(m):
    a,b,c = map(int, input().split())
    graph.append([c,a-1,b-1])

graph.sort(reverse = True)
result = 0
for i in graph:
    cost, start, end = i
    union_parent(parent,start,end)
    result = cost
    if find_parent(parent,s-1) == find_parent(parent,e-1):
        break
        
if parent[s-1] == parent[e-1]:
    print(result)
else:
    print(0)
    
'''
정말 오래걸린 문제... find_parent(parent,x)와 find_parent(parent,parent[x])는 서로
다를 때에만 동일한 데, 이 부분에서 계속 실수해서 오래 걸렸다
'''