#Q44 행성 터널
#https://www.acmicpc.net/problem/2887
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

n = int(input())
planets = []
parent = [i for i in range(n)]

for i in range(n):
    a,b,c = map(int, input().split())
    planets.append([a,b,c,i])

graph = []
for j in range(3):
    planets.sort(key = lambda x : x[j])
    start = planets[0][3]
    for i in range(1,n):
        end = planets[i][3]
        graph.append([abs(planets[i][j]-planets[i-1][j]),start,end])
        start = end
        
result = 0
cnt = 0
graph.sort()

for cost, x, y in graph:
    if find_parent(parent,x) != find_parent(parent,y):
        union_parent(parent,x,y)
        result+=cost
        cnt+=1
    if cnt == n-1:
        break
        
print(result)