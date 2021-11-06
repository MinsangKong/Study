def solution(arr):
    counter = [0]*4
    answer = []
    for i in range(len(arr)):
        counter[arr[i]] += 1
    target = max(counter)
    for i in range(1,4):
        answer.append(target-counter[i])
    return answer