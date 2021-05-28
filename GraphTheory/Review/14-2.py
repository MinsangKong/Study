import sys
from collections import deque
input = sys.stdin.readline

t = int(input())

result = []

for s in range(t):
  
    k , m , p = map(int, input().split())

    graph = [[] for i in range(m + 1)]
    inDegree = [0] * (m + 1)
    strahler = [[0 , 0] for i in range(m + 1)]

    for _ in range(p):
        a , b = map(int , input().split())
        graph[a].append(b)
        inDegree[b] += 1

    queue = deque()

    for i in range(1 , m + 1):
        if inDegree[i] == 0:
            queue.append(i)
            strahler[i][0] , strahler[i][1] = 1 , 1

    while queue:
        now = queue.popleft()
        for item in graph[now]:
            inDegree[item] -= 1
            if strahler[now][0] > strahler[item][0]:
                strahler[item][0] = strahler[now][0]
                strahler[item][1] = 1
            elif strahler[now][0] == strahler[item][0]:
                strahler[item][1] += 1
                if strahler[item][1] >= 2:
                    strahler[item][0] = strahler[now][0] + 1
                    strahler[item][1] = 0
            if inDegree[item] == 0:
                queue.append(item)
  
    result.append((k , strahler[m][0]))

for item in result:
    print(item[0] , item[1])

'''
똑같은 위상 정렬이지만 굳이 2개의 배열을 지정하지 않고 2차원 배열을 사용하여 간략하게
적용했기 때문에 근소하게 빨랐다.
'''