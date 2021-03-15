#https://www.acmicpc.net/problem/10423
#백준 10423번 전기가 부족해(그래프 이론, 크루스컬)
#import sys
#input = sys.stdin.readline

def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] == -1:
        return -1
    elif parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n, m, k = map(int, input().split())
plant = list(map(int, input().split()))
cable = []
parent = [0] * (n + 1)
result = 0

for i in range(1, n + 1):
    parent[i] = i

for i in plant:
    #발전소가 있는 node는  -1로 변경
    parent[i] = -1

for _ in range(m):
    u, v, w = map(int, input().split())
    cable.append((w, u, v))

cable.sort()

for edge in cable:
    w, u, v = edge
    if find_parent(parent, u) != find_parent(parent, v):
        union_parent(parent, u, v)
        result += w
print(result)
'''
고발전소가 있는 node를 어떻게 처리해야할지 고민을 좀많이 하긴 했는데 생각보다
풀 만한 문제였다. root node를 -1로 변경함으로써 cycle이 서로 안생기도록 하고
크루스컬 알고리즘을 적용해서 문제를 해결하니까 간단했다. 
'''