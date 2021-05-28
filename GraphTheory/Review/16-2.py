#https://www.acmicpc.net/problem/2637
#백준 2637번 장난감조립(위상정렬)
#import sys
#input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[] for _ in range(n)]
indegree = [0]*n
dp = [0]*n

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a-1].append([b-1,c])
    indegree[b-1]+=1
    
q = [n-1]
dp[n-1] = 1

while q:
    now = q.pop()
    for base, cnt in graph[now]:
        dp[base] += dp[now]*cnt
        indegree[base] -= 1
        if indegree[base] == 0:
            q.append(base)

for i in range(n):
    if not graph[i]:
        print(i+1, dp[i])
'''
dp를 활용해서 했으면 훨씬 효율적이었는데 생각이 안났다...
후... 이럴 때마다 너무 지친다... dict()활용해서 재귀를 돌려도 문제 없을 줄 알았는데
단순하게 dp를 사용하면 더 빨랐을 줄이야...
'''