def solution(s):
    length = len(s)
    answer = []
    l,r = 1,length-1
    cnt = 1
    while l < r : 
        if s[l] != s[0] and s[r] != s[0]:
            break
        if s[l] == s[0] :
            l += 1
            cnt += 1
        if s[r] == s[0]:
            r -= 1
            cnt += 1
    if l == r :
        if s[l] == s[0] :
            cnt += 1
        else:
            answer.append(1)
        answer.append(cnt)
        return sorted(answer)
    answer.append(cnt)
    cnt = 1

    for i in range(l,r+1):
        if i == r:
            answer.append(cnt)
            break
        if s[i] == s[i+1]:
            cnt += 1
        else:
            answer.append(cnt)
            cnt = 1
    return sorted(answer)