#https://www.acmicpc.net/problem/11724
#백준 11724번 연결 요소의 개수(그래프 이론,dfs, 사이클)
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

v, e = map(int, input().split())
parent = [0] * (v + 1) 

for i in range(1, v + 1):
    parent[i] = i
    
for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)
    
for i in range(1,v+1):
    find_parent(parent, i)
    
print(len(set(parent))-1)
'''
dfs로 풀지 않고 일부러 root 찾기로 해결했는데 시간적인 면에서 훨씬 비효율적이다.

'''