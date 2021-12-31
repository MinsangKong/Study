n, m = 5, 4
ans = 0
selected = []
day_map = {'MO': 0, 'TU': 1, 'WE': 2, 'TH': 3, 'FR': 4}
def conv(tz):
    return day_map[tz[:2]] * 60 * 24 + int(tz[3:5]) * 60 + int(tz[6:8])
def parse(tz):
    if len(tz) == 8:
        v = conv(tz)
        return [(v, v + 90), (v + 90, v + 180)]
    else:
        v1 = conv(tz[:8])
        v2 = conv(tz[9:])
        return [(v1, v1 + 90), (v2, v2 + 90)]
def conflict(A, B):  # A, B는 모두 시간 (요일 + 시간 + 분)
    A = parse(A)
    B = parse(B)
    for a in A:
        for b in B:
            if max(a[0], b[0]) < min(a[1], b[1]):
                return True
    return False
def dfs(idx, schedule):
    if idx == len(schedule):
        return 1
    ret = 0
    for j in schedule[idx]:  # j 시간에 들을 것
        flag = True
        for k in selected:  # k 시간에 이미 다른 과목 들음
            if conflict(j, k):  # 겹치면 실패
                flag = False
        if flag:  # 안 겹치면 재귀호출
            selected.append(j)
            ret += dfs(idx + 1, schedule)
            selected.pop()
    return ret
def solution(schedule):
    return dfs(0, schedule)