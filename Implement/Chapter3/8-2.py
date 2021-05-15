#DP 활용
from collections import defaultdict

def solution(n, weak, dist):
    dic = defaultdict(list)
    dic[0].append(tuple(weak))
    dist.sort()
    level,maxlevel = 0,len(dist)
    while level!=maxlevel and dist and () not in dic[level]:
        d = dist.pop()
        temp = set()
        for weak in dic[level]:
            temp |= {tuple(j for j in weak if not (weak[i]<=j<=weak[i]+d or weak[i]<=j+n<=weak[i]+d)) for i in range(len(weak))}
        level +=1
        dic[level].extend(list(temp))
    result = sorted(dic.keys())[-1]
    if () not in dic[result] : return -1
    return result