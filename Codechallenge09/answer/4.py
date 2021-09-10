def solve(a, last, n):
    dy = [0 for _ in range(n)]
    dy[0] = 1
    accum = [dict() for _ in range(n)]
    for i in range(0, n):
        SUM, cnt = a[last + i], 1
        j = i
        accum[i][a[last + i]] = 1
        if i >= 1:
            dy[i] = dy[i - 1]
        while j >= 1:
            if SUM not in accum[j - 1]:
                break
            v = accum[j - 1][SUM]
            cnt += v
            SUM *= 2
            j -= v
            if j - 1 >= 0 and j - 1 < len(dy):
                dy[i] += dy[j - 1]
            else:
                dy[i] += 1
            dy[i] %= 1000000007
            accum[i][SUM] = cnt
    return dy[n - 1]
def solution(a, s):
    res = []
    last = 0
    for t in s:
        res.append(solve(a, last, t))
        last += t
    return res