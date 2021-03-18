def solution(food_times, k):
    answer = 1
    count = 0
    while count <= k:
        if sum(food_times) <= 0:
            answer=-1
            break
        if food_times[answer-1] <= 0:
            answer+=1
            if answer > len(food_times):
                answer=1
            continue
        else :
            if count == k:
                break
            food_times[answer-1] -=1
            answer+=1
            if answer > len(food_times):
                answer=1
            count+=1
    return answer
'''
정확성은 완벽하게 클리어 했지만, 효율성 면에서 다 틀렸다.
해설 코드를 보니까 효율성 면에서 엉망일만했다. 굳이 모든 코드를 확인 안해도 하나의 음식을 클리어하면 그 시간을 그만큼 빼는 식으로 했으면
효율성을 만족할 수 있었다. 처음 문제를 보고 엄청 쉬워보이는 문제는 절대로 직관적으로 풀면 안된다. 문제를 보고 식을 도출해야 한다...

'''