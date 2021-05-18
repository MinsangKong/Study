from collections import deque

def solve(N,K):
    visited = [0] * (100001)
    visited[N] = 1
    de = deque([N])

    while de:
        cur = de.popleft()
        if cur == K:
            return visited[K]-1
        if 2*cur <= 100000 and not visited[2*cur]:
            visited[2*cur] = visited[cur]
            de.appendleft(2*cur)
        if cur-1 >= 0 and not visited[cur-1]:
            visited[cur-1] = visited[cur]+1
            de.append(cur-1)
        if cur+1 <= 100000 and not visited[cur+1]:
            visited[cur+1] = visited[cur]+1
            de.append(cur+1)

N, K = [int(x) for x in input().split()]
print(solve(N,K))
'''
의외로 속도면에서는 heapq보다 deque가 더 빨랐다. 근소한 차이 30ms 정도
'''