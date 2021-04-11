#https://programmers.co.kr/learn/courses/30/lessons/42839
#프로그래머스 소수 찾기
from itertools import permutations
import math

def check(n):
    k = math.sqrt(n)
    if n < 2: 
        return False

    for i in range(2, int(k)+1):
        if n % i == 0:
            return False
    return True

def solution(numbers):
    answer = []
    for k in range(1, len(numbers)+1):
        perlist = list(map(''.join, permutations(list(numbers), k)))
        perlist_s = list(set(perlist))
        for i in perlist_s:
            if check(int(i)):
                if int(i) not in answer:
                    answer.append(int(i))

    answer = len(answer)

    return answer