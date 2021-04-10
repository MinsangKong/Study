from collections import deque
import sys
input = sys.stdin.readline


def bfs():
    q = deque([s])
    dp[s] = 1
    while q:
        start = q.popleft()
        if start == g:
            print(dp[g] - 1)
            return

        up = start + u
        down = start - d
        if up <= f and not dp[up]:
            q.append(up)
            dp[up] = dp[start] + 1
        if down > 0 and not dp[down]:
            q.append(down)
            dp[down] = dp[start] + 1

    else:
        print("use the stairs")
        return


f, s, g, u, d = map(int, input().split())
dp = [0] * (f + 1)
bfs()
'''
경우의 수가 적은 경우에는 빠르게 up = start + u, down = start - d하는 방식으로
풀면 실행속도가 훨씬 빨랐다.
'''