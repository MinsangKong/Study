import sys
input = sys.stdin.readline

def dfs(start, cur):
    if start != cur:
        edge_cnt[start] += 1
        edge_cnt[cur] += 1
    visited[cur] = True
    for w in graph[cur]:
        if not visited[w]:
            dfs(start, w)


N, M = list(map(int, input().split()))
graph = [[] for _ in range(N+1)]
ans = 0
for _ in range(M):
    a, b = list(map(int, input().split()))
    graph[a].append(b)

edge_cnt = [0] * (N+1)
for node in range(1, N+1):
    visited = [False] * (N+1)
    dfs(node, node)

for node in range(1, N+1):
    if edge_cnt[node] == N-1:
        ans += 1

print(ans)
'''
가장 최적의 풀이법. 코테에서 풀 때 이렇게 풀게 노력하자
'''