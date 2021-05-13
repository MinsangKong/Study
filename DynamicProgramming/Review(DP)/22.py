#https://www.acmicpc.net/problem/1516
#백준 1516번 게임 개발(DP,위상정렬)
#import sys
#input = sys.stdin.readline
from collections import defaultdict, deque

n = int(input())
answer = [0] * (n+1)
cost = [0] * (n+1)
degree = [0] * (n+1)
q = deque()

graph = defaultdict(list)
for i in range(1,n+1):
    temp = list(map(int, input().split()))
    cost[i] = temp[0]

    for element in temp[1:-1]:
        graph[element].append(i)
        degree[i] += 1


for i in range(1,n+1):
    if degree[i] == 0:
        q.append(i)
        answer[i] = cost[i]

while q:
    now = q.popleft()
    for element in graph[now]:
        degree[element] -= 1
        answer[element] = max(answer[element], cost[element] + answer[now])

        if degree[element] == 0:
            q.append(element)


for i in range(1, len(answer)):
    print(answer[i])