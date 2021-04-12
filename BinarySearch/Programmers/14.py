#https://programmers.co.kr/learn/courses/30/lessons/42747
#level 2 H-index(정렬)
def solution(citations):
    citations.sort()
    answer = 0
    for i in range(0, citations[-1]+1): 
        h=0
        k=0
        for j in citations: # i번 이상 인용된 논문수인 h를 구함
            if j>=i:
                h+=1
        for j in citations:# i번 이하 인용된 논문수인 k를 구함
            if j<=i:
                k+=1
        if h >= i and k <= i : # h가 i 이상이고 k가 i 이하인 조건을 만족하는 값을 구함
            if i>answer : 
                answer=i # 그중에 최댓값을 구함
    if citations[0] >= len(citations) :  #최소값이 논문의 수보다 길면 자동적으로 길이가 h
        answer = len(citations)
    return answer