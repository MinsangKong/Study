import sys

sys.setrecursionlimit(10**5)
input = sys.stdin.readline
flush = sys.stdout.flush

def cost(v):
    if dp[v] is not None:
        return dp[v]

    res = 0
    for w in nbhd[v]:
        if cost(w) > res:
            res = cost(w)
    dp[v] = res + d[v]
    return dp[v]

for _ in range(int(input())):
    n, k = map(int, input().split())
    d = [0] + list(map(int, input().split()))
    dp = [None] * (n + 1)
    nbhd = [[] for _ in range(n + 1)]
    for _ in range(k):
        a, b = map(int, input().split())
        nbhd[b].append(a)
    print(cost(int(input())))
'''
DP로 처리하면 위상정렬보다 빠르게 풀 수 있다.
'''