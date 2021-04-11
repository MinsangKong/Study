#https://www.acmicpc.net/problem/2623
#백준 2623번 음악 프로그램(그래프 이론, DFS)
import sys
#input = sys.stdin.readline

def dfs(nn):
    if is_visited[nn]: #방문했던것을 다시 방문하는 것은 cycle이 발생했기 때문에
        print(0)
        sys.exit(0)

    if finished[nn]:
        return

    is_visited[nn] = True
    for i in graph[nn]:
        dfs(i)

    stack.append(nn)
    finished[nn] = True
    is_visited[nn] = False


N, M = map(int, input().split())
graph = {i: [] for i in range(N)}
for _ in range(M):
    line = list(map(int, input().split()))
    for i in range(1, len(line) - 1):
        graph[line[i] - 1].append(line[i + 1] - 1)

finished = [False] * N
is_visited = [False] * N
stack = []

for i in range(N):
    if finished[i]:
        continue
    dfs(i)

stack = map(lambda x: x+1, stack)
stack = list(map(str, stack))
stack.reverse()

print('\n'.join(stack))
'''
이 문제도 마찬가지로 DFS로 해결할 수 있는 문제였다. DFS를 적용하더라도 마찬가지로
cycle 여부를 체크해줘야하고 출력할 때에는 역순으로 해줘야 한다.
'''