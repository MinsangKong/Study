def solution(s):
    answer = []
    nums = ['zero','one','two','three','four','five','six','seven','eight','nine']
    check = ""
    for i in s:
        if '0' <= i <= '9':
            if check != "":
                search = ""
                for j in check:
                    search+=j
                    if search in nums:
                        answer.append(str(nums.index(search)))
                        search = ""
                check = ""
            answer.append(i)
        else:
            check+=i
    if check != "":
        search = ""
        for j in check:
            search+=j
            if search in nums:
                answer.append(str(nums.index(search))) 
                search = ""
    return int("".join(answer))
print(solution("onezeroseveneight"))