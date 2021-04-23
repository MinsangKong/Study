def solution(N, stages):
    result = {}
    denominator = len(stages)
    for stage in range(1, N+1):
        if denominator != 0:
            count = stages.count(stage)
            result[stage] = count / denominator
            denominator -= count
        else:
            result[stage] = 0
    return sorted(result, key=lambda x : result[x], reverse=True)
'''
다른 사람들의 코드를 보니까 굳이 리스트로 비교하지 말고 dictionary로 비교한 다음 정렬할 때 lambda x : 
result[x]로 하면 value값들을 기준으로 key값들이 정렬이 되기 때문에 시간적인 면에서 훨씬 효율적이다.
'''