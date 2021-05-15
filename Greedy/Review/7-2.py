#https://www.acmicpc.net/problem/13413
#백준 13413번 오셀로 재배치(그리디)

import sys

case = int(input())

def check(val1, val2):
    cnt = 0
    for i in range(len(val1)):
        if val1[i] != val2[i]:
            cnt += 1
    
    return cnt

for _ in range(case):
    N = int(input())
    std = input()
    goal = input()

    w1, w2 = std.count("W"), goal.count("W")
    b1, b2 = N - w1, N-w2

    if w1 == 0 or w2 == 0:
        print(abs(w1-w2))
        continue

    res = check(std, goal)
    if w1 == w2:
        print(res//2)
    else:
        print((res-abs(w1-w2))//2 + abs(w1-w2))
        
'''
남의 코드를 보고 비교해보니까 이렇게 간단하게 답이 나왔다.
직관적으로 문제를 푸는게 아니라 이것저것 테스트해보니까 시간만 엄청 오래 걸렸다.
'''