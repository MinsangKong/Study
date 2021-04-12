#https://programmers.co.kr/learn/courses/30/lessons/42748
#level 1 K번째 수(정렬)
def solution(array, commands):
    answer = []
    for m in commands:
        i = m[0]
        j = m[1]
        k = m[2]
        arr = array[i-1:j]
        arr.sort()
        num = arr[k-1]
        answer.append(num)
    return answer