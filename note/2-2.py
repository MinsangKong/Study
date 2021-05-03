def solution(array):
    length = len(array)
    
    if length == 0:
        return []
    elif length == 1:
        return [-1]
    elif length == 2:
        if array[0] > array[1]:
            return [-1, 0]
        else:
            return [1, -1]
        
    check_l = []
    check_r = []
    dp = [-1] * length
    for i in range(length):
        num = array[i]
        while check_l and array[check_l[-1]] <= num:
            check_l.pop()
        if check_l:
            dp[i] =check_l[-1]
        check_l.append(i)
    for i in range(length-1,-1,-1):
        num = array[i]
        while check_r and array[check_r[-1]] <= num:
            check_r.pop()
        if check_r:
            if dp[i] != -1 :
                dp[i] = min(dp[i], check_r[-1])
            else:
                dp[i] = check_r[-1]
        check_r.append(i)    
    return dp
print(solution([5,4,2,1,3]))