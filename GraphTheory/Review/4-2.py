import sys

n = int(sys.stdin.readline())
dis = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
visit = [0] * n
dis2 = [100000001] * n
dis2[0] = 0


def solution():
    answer = 0

    for _ in range(n):
        minv = 100000001
        idx = -1
        for i in range(n):
            if not visit[i] and minv > dis2[i]:
                minv = dis2[i]
                idx = i
        answer += minv
        visit[idx] = 1
        for i in range(n):
            if not visit[i] and dis2[i] > dis[idx][i]:
                dis2[i] = dis[idx][i]
    return answer


ans = solution()
print(ans)