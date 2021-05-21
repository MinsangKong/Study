import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split(' '))
edge = [[] for i in range(N + 1)]
for i in range(M):
    a, b = map(int, input().split(' '))
    edge[a].append(b)
    edge[b].append(a)

answer = [[0 for i in range(N + 1)] for i in range(N + 1)]
# print(edge)
def bfs(i):
    visited = [0 for i in range(N + 1)]
    q = deque()
    q.append((i, 0))
    visited[i] = 1
    while q:
        here, v = q.popleft()
        for there in edge[here]:
            if visited[there]:
                continue
            visited[there] = v + 1
            q.append((there, v + 1))
    visited[i] = 0
    return visited

def min_sum(a, b):
    answer = 0
    for i in range(1, len(a)):
        answer += min(a[i], b[i])
    return answer
bfss = []
for i in range(1, N + 1):
    bfss.append(bfs(i))

answer = [0, 1, min_sum(bfss[0], bfss[1])]
for i in range(len(bfss)):
    for j in range(i + 1, len(bfss)):
        temp = min_sum(bfss[i], bfss[j])
        if temp < answer[2]:
            answer = [i, j, temp]

answer[0] += 1
answer[1] += 1
answer[2] *= 2
print(*answer)