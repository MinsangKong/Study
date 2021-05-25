#https://www.acmicpc.net/problem/16202
#백준 16202번 MST게임(MST, 크루스컬)
#import sys
#input = sys.stdin.readline

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n,m,k = map(int, input().split())
graph = []

for i in range(m):
    a,b = map(int, input().split())
    graph.append([i+1,a-1,b-1])
    
result = []

for i in range(k):
    point = 0
    parent = [k for k in range(n)]
    for j in range(i,m):
        cost, s, e = graph[j]
        if find_parent(parent, s) != find_parent(parent, e):
            union_parent(parent, s, e)
            point+=cost
    flag = True
    for j in range(1,n):
        if find_parent(parent,j) != find_parent(parent,j-1):
            flag = False
            break
    if flag:
        result.append(point)
    else:
        result.append(0)
        
print(*result)
'''
flag를 추가하지 않고 union 연산을 진행할 때마다 1을 더하는 식으로 하면 cycle이 
발생하는 경우에는 결과값이 n-1보다 작아지기 때문에 더 빠르게 답을 구할 수 있다.
'''