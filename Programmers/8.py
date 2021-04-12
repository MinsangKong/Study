#https://programmers.co.kr/learn/courses/30/lessons/42842
#level 2 카펫(완전탐색)
def solution(brown, yellow):
    s = brown + yellow
    for i in range(s,2,-1): # 가로는 세로 이상이어야 하기 때문에 기준을 가로로
        if s % i == 0:
            a= s // i
            if yellow == (i-2)*(a-2):
                return [i, a]