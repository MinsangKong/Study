def solution(n, info):
    answer = []
    score = 0
    arrows= [0]*11

    def dfs(n,idx):
        nonlocal score
        nonlocal answer
        if n == 0 or idx < 0 :
            apeach = 0
            ryan = 0
            for i in range(11):
                if arrows[i] > info[i]:
                    ryan += 10-i
                elif arrows[i] < info[i]:
                    apeach += 10-i
            if score < ryan - apeach:
                score = ryan - apeach
                answer = arrows[:]
                if n > 0:
                    answer[10] += n
            return
        if info[idx] < n :
            arrows[idx] = info[idx]+1
            dfs(n-arrows[idx],idx-1)
            arrows [idx] = 0 
        dfs(n,idx-1)
    dfs(n,10)
    if answer :
        return answer
    else:
        return [-1]

print(solution(5,[2,1,1,1,0,0,0,0,0,0,0]))