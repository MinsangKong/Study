def solution(a, b, g, s, w, t):
    n = len(g)
    l, r = 0, 200000000000000
    ans = r
    while l <= r:
        mid = (l + r) // 2
        tot, G, S = 0, 0, 0
        for i in range(n):
            # cnt = mid // (t[i] * 2)
            # if mid % (t[i] * 2) >= t[i]:
            #     cnt += 1
            cnt = (mid * 2) // (t[i] * 2)
            # upper := 이 트럭이 운반할 수 있는 "광물"의 최대량
            upper = min(cnt * w[i], g[i] + s[i])
            tot += upper
            G += min(g[i], upper)
            S += min(s[i], upper)
        if tot >= a + b and G >= a and S >= b:
            ans = min(ans, mid)
            r = mid - 1
        else:
            l = mid + 1
    return ans