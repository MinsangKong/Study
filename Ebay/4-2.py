#4번
def solution(n, k, bulbs):
    answer = 0
    light = {'R': 0,'G': 1,'B': 2}
    cur = [0] * n
    for i in range(n):
        cur[i] = light[bulbs[i]]
    prefix = [0] * (n + 1)
    if cur[0] == 1:
        prefix[0] = 2
        prefix[k] = -2
        answer += 2
    elif cur[0] == 2:
        prefix[0] = 1
        prefix[k] = -1
        answer += 1
    for i in range(1, n - k + 1):
        prefix[i] += prefix[i - 1]
        cnt = (3 - (cur[i] + prefix[i]) % 3) % 3
        prefix[i] += cnt
        prefix[i + k] -= cnt
        answer += cnt
    for i in range(n - k + 1, n + 1):
        prefix[i] += prefix[i - 1]
    for i in range(n):
        if (cur[i] + prefix[i]) % 3:
            return -1
    return answer
print(solution(4,3,"BBBR"))