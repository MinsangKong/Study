#Q30 가사 검색
#https://programmers.co.kr/learn/courses/30/lessons/60060
def bisect_left(string):
    start = 0
    end = len(string)-1
    result = 0
    while start <= end:
        mid = (start+end)//2
        if string[mid] != '?':
            end = mid -1
        else:
            result = mid
            start = mid+1
    return result

def bisect_right(string):
    start = 0
    end = len(string)-1
    result = 0
    while start <= end:
        mid = (start+end)//2
        if string[mid] != '?':
            start = mid +1
        else:
            result = mid
            end = mid-1
    return result

def solution(words, queries):
    answer = []
    for query in queries:
        start = 0
        end = len(query)-1
        if query[start] == '?':
            end = bisect_left(query)
        else:
            start = bisect_right(query)
        cnt = 0
        print(start,end)
        for word in words:
            if len(query) != len(word):
                continue
            elif start == 0:
                if end == len(query)-2:
                    if query[len(query)-1] == word[len(word)-1]:
                        cnt+=1
                elif word[end+1:] == query[end+1:]:
                    cnt+=1
            else:
                if start == 1:
                    if query[0] == word[0]:
                        cnt+=1
                elif word[:start] == query[:start]:
                    cnt+=1
                    
        answer.append(cnt)
    return answer
'''
맨 처음에 푼 방법은 효율성 1,2,3에서 시간초과떠서 55점 획득.
'''