#https://programmers.co.kr/learn/courses/30/lessons/42842
#프로그래머스 카펫
def solution(brown, yellow):
    s = brown + yellow
    for i in range(s,2,-1): # 가로는 세로 이상이어야 하기 때문에 기준을 가로로
        if s % i == 0:
            a= s // i
            if yellow == (i-2)*(a-2):
                return [i, a]