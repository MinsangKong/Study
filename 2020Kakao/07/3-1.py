#Q3 보석 쇼핑
#https://programmers.co.kr/learn/courses/30/lessons/67258
def solution(gems):
    answer = [0,10001]
    length = len(gems)
    total = len(set(gems))
    check = {gems[0]: 1}
    start, end = 0, 0
    while start < length and end < length:
        if len(check) < total:
            if end == length - 1:
                break
            end += 1
            if gems[end] in check:
                check[gems[end]] += 1
            else:
                check[gems[end]] = 1
        else:
            if end-start < answer[1]-answer[0]:
                answer[0], answer[1] = start+1, end+1
            if check[gems[start]] == 1:
                del check[gems[start]]
            else:
                check[gems[start]] -= 1
            start += 1
    return answer
print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))