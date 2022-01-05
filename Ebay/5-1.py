def solution(P):
    length = len(P)
    visited = [-1]*length
    ans = [0]*length
    def dfs(idx, visited, cnt):
        nonlocal ans
        if cnt == 0 :
            ans[visited[0]] = 1
            return
        if idx > length :
            return 
        if visited[idx] != -1:
            dfs(idx+1,visited,cnt)
        for i in range(idx+1,length):
            if visited[i] == -1:
                pal = P[idx]+P[i]
                repal = P[i]+P[idx]
                if pal == pal[::-1]:
                    visited[idx] = i
                    visited[i] = idx
                    dfs(idx+1,visited,cnt-2)
                    visited[i] = -1
                    visited[idx] = -1
                    continue
                elif repal == repal[::-1]:
                    visited[idx] = i
                    visited[i] = idx
                    dfs(idx+1,visited,cnt-2)
                    visited[i] = -1
                    visited[idx] = -1
                    
    dfs(0,visited,length)
    result = []
    for i in range(length):
        if ans[i]:
            result.append(P[i])
    return result

print(solution(["21","123","111","11"]))