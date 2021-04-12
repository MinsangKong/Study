#https://programmers.co.kr/learn/courses/30/lessons/42746
#level 2 가장 큰 수(정렬)
def solution(numbers):
    l = lambda x: x*3 
    str_numbers = sorted(list(map(str, numbers)), reverse=True, key = l)
    return str(int(''.join(str_numbers)))