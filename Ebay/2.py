
def solution(stones, k):
    answer = []
    length = len(stones)
    def dfs(cnt, oper):
        nonlocal answer

        if stones[-1] == k :
            if sum(stones[:-1]) == 0 :
                answer.append(oper)
                return
            else :
                idx = -1
                num = int(1e9)
                for i in range(length):
                    if stones[


    
    return answer