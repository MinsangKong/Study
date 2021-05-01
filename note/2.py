import bisect
def solution(array):
    length = len(array)
    answer = []
    
    if length == 0:
        return answer
    elif length == 1:
        return [-1]
    
    for i in range(length):
        check = -1
        if i == 0:
            for j in range(1,length):
                if array[i] < array[j]:
                    check=j
                    break
        elif i == length-1:
            for j in range(length-1,-1,-1):
                if array[i] < array[j]:
                    check=j
                    break
        else:
            check2 = -1
            for j in range(i-1,-1,-1):
                if array[i] < array[j]:
                    check = j
                    break
            for j in range(i+1,length):
                if array[i] < array[j]:
                    check2 = j
                    break      
            if check != -1 and check2 != -1:
                check = min(check,check2)
            elif check == -1:
                check = check2
        answer.append(check)
    return answer
print(solution(	[1, 2, 3, 4, 5]))