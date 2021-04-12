#https://programmers.co.kr/learn/courses/30/lessons/42862
#level 1 체육복(그리디)
def solution(n, lost, reserve):
    answer = 0

    answer=n-len(lost)

    j=0

    while True:
        if(j>=len(lost) or (len(reserve)==0)):
            break
        if lost[j] in reserve:
            answer=answer+1
            reserve.remove(lost[j])
            lost.remove(lost[j])
            continue
        j=j+1

    i=0
    while True:
        if(i>=len(lost) or (len(reserve)==0)):
                break
        if (lost[i]-1) in reserve:
            answer=answer+1
            reserve.remove(lost[i]-1)
            i=i+1
            continue
        if (lost[i]+1) in reserve:
            answer=answer+1
            reserve.remove(lost[i]+1)
            i=i+1
            continue
        else:
            i=i+1

    return answer
