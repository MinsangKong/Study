#https://programmers.co.kr/learn/courses/30/lessons/42840
#프로그래머스 모의고사
def solution(answers):
    answer = []
    case1 = [1,2,3,4,5]
    count1 = 0
    case2 = [2,1,2,3,2,4,2,5]
    count2 = 0
    case3 = [3,3,1,1,2,2,4,4,5,5]
    count3 = 0
    for i in range(len(answers)):
        if answers[i] == case1[i%5] :
            count1+=1
        if answers[i] == case2[i%8] :
            count2+=1
        if answers[i] == case3[i%10] :
            count3+=1

    if count3 == count2 == count1 :
        answer.extend([1,2,3])
    elif count1 > count2 and count1 > count3 :
        answer.append(1)
    elif count2 > count1 and count2 > count3 :
        answer.append(2)
    elif count3 > count1 and count3 > count2 :
        answer.append(3)
    elif count1 == count2:
        answer.extend([1,2])
    elif count1 == count3:
        answer.extend([1,3])
    elif count2 == count3:
        answer.extend([2,3])
    return answer