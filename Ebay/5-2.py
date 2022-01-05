#5번
def solution(P):
    length = len(P)
    visited = [-1] * length
    ans = [0] * length
    pos = [[0 for _ in range(length)] for _ in range(length)]
    def preprocess():
        for i in range(length):
            for j in range(length):
                if i == j: continue
                x = P[i] + P[j]
                if x == x[::-1]:
                    pos[i][j] = 1
                    pos[j][i] = 1

    def dfs(idx, visited, cnt):
        nonlocal ans
        if visited[0] != -1 and ans[visited[0]] == 1:
            return
        if cnt == 0:
            ans[visited[0]] = 1
            return
        if idx > length :
            return 
        if visited[idx] != -1:
            dfs(idx + 1, visited, cnt)
        for i in range(idx + 1, length):
            if visited[i] == -1:
                if pos[idx][i] == 1:
                    visited[idx] = i
                    visited[i] = idx
                    dfs(idx + 1, visited, cnt - 2)
                    visited[i] = -1
                    visited[idx] = -1
                    
    preprocess()
    dfs(0,visited,length)
    return [P[i] for i in range(length) if ans[i]]
print(solution(["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"]))