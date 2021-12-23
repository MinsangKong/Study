#https://programmers.co.kr/learn/courses/30/lessons/17681
#카카오 2018 blind 비밀지도
def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        case1 = bin(arr1[i])[2:]
        data = ''
        if len(case1) != n :
            case1 = '0'*(n-len(case1))+case1
        case2 = bin(arr2[i])[2:]
        if len(case2) != n :
            case2 = '0'*(n-len(case2))+case2
        print(case1,case2)
        for j in range(n):
            if case1[j] == '1' or case2[j] == '1':
                data += '#'
            else:
                data += ' '
        answer.append(data)
    return answer