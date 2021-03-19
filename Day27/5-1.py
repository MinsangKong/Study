#https://www.acmicpc.net/problem/4386
#백준 4386번 별자리 만들기(그래프이론, 크루스컬)
#import sys
#input = sys.stdin.readline

def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
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

n = int(input())
stars = []
parent = [0] *(n + 1)
costs = {} #별들을 잇는 비용을 저장하기 쉽게하기 위해 딕셔너리로
result = 0

for i in range(1, n+1):
    parent[i] = i

for i in range(n):
    stars.append(list(map(float, input().split())))
    
for i in range(n):
    for j in range(i+1, n):
        a = stars[i]
        b = stars[j]
        dist = round(((a[0] - b[0])**2 + (a[1] - b[1])**2)**0.5, 2)
        costs[(i, j)] = dist
#costs[0] = (i,j) costs[1] = dist
costs = sorted(costs.items(), key = lambda x: x[1])

for cost in costs:
    x,y = cost[0]
    dist = cost[1]
    if find_parent(parent, x) != find_parent(parent, y):
        union_parent(parent, x, y)
        result += dist
print(result)
'''
하다가 중간에 막혀서 계속 생각해보니까 입력받은 정보는 node에 관한 정보가 아니라
간선에 대한 정보이기 때문에 바로 result에서 dist를 구해서 저장하는게 아니라 따로
정렬을 해줘야 했었다. 처음 관점을 잘 못 잡았더니 시간이 생각보다 오래 걸렸다.
그래도 기존에 풀어봤던 문제와 다르게 생각 할 수 있어서 도움이 많이 되었다.
https://developmentdiary.tistory.com/448 여기에서는 prime을 적용해서 해결
'''