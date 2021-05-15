#Q25번 실패율
def solution(N, stages):
    length = len(stages)
    check = []
    for i in range(1,N+1):
        n = stages.count(i)
        if length != 0:
            check.append((n/length,i))
            length-=n
        else:
            check.append((0,i))
    check.sort(key = lambda x : -x[0])
    answer = []
    for i in range(N):
        answer.append(check[i][1])
    return answer