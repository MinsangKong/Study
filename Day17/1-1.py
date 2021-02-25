#https://www.acmicpc.net/problem/14496 최단 경로
#백준 14496번 그대, 그머가 되어
#다익스트라로 도저히 못 풀겠어서 bfs로 문제를 품
import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    q = deque()
    q.append(a)
    visited = [0]*(N+1)
    #word[i]에 있으면 그 원소를 q에 넣고 다시 돌리기
    while q:
        x = q.popleft()
        if x == b : return visited[x]
        for j in word[x] :
            if visited[j] == 0 :
                q.append(j)
                visited[j] = visited[x]+1
    return -1

a, b = map(int, input().split())
N, M = map(int, input().split())
word = [[] for i in range(N+1)]
for i in range(M):
    x,y = map(int,input().split())
    word[x].append(y)
    word[y].append(x)

print(bfs())