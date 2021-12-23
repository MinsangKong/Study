#https://programmers.co.kr/learn/courses/30/lessons/17682
#카카오 2018 blind 다트 게임

def solution(dartResult):
    length = len(dartResult)
    result = 0
    rule = {'S':1, 'D':2, 'T':3}
    double = [0]*3
    minus = [0]*3
    score = [0]*3
    idx = -1
    last = 0
    for i in range(length):
        if dartResult[i].isdigit():
            if last :
                last += dartResult[i]
            else:
                idx += 1
                last = dartResult[i]
        elif dartResult[i].isalpha():
            num = int(last)
            last = 0
            score[idx] = num**rule[dartResult[i]]
        else:
            if idx == 0:
                if dartResult[i] == '*' :
                    double[idx] += 1
                else:
                    minus[idx] += 1
            else:
                if dartResult[i] == '*' :
                    double[idx] += 1
                    double[idx-1] += 1
                else:
                    minus[idx] += 1
                
    #print(score)
    for i in range(3):
        if double[i] > 0 :
            score[i] *= 2*double[i]
        if minus[i] > 0 :
            score[i]*= -1
        result += score[i]
    return result