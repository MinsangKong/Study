#https://www.acmicpc.net/problem/14567
#백준 14567번 선수과목(그래프이론, 위상정렬)
#import sys
#input = sys.stdin.readline
from collections import deque
import copy

n, m = map(int, input().split())
indegree = [0] * (n + 1)
graph = [[] for i in range(n + 1)]
time = [1] * (n + 1)

for i in range(1, m + 1):
    a, b = map(int, input().split())
    indegree[b] += 1
    graph[a].append(b)
    
def topology_sort():
    result = copy.deepcopy(time)
    q = deque()
    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)
    while q:
        now = q.popleft()
        for i in graph[now]:
            result[i] = max(result[i], result[now] + time[i])
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)
    for i in range(1, n + 1):
        print(result[i], end =' ')
topology_sort()
'''
같은 알고리즘이여도 result 배열을 전역으로 선언한 것과 copy.deepcopy로 복사한
result 배열은 속도 차이가 존재한다. copy.deepcopy로 복사한 배열이 50ms정도
더 빠르다. 
'''