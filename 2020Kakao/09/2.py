def solution(n, k):
    answer = 0
    bases = "0123456789"
    def changer(num, base) :
        q, r = divmod(num, base)
        if q == 0 :
            return bases[r]
        else :
            return changer(q, base)+ bases[r] 
    convertedN = changer(n,k)
    print(convertedN)
    temp = ""
    nums = []
    for i in range(len(convertedN)):
        if convertedN[i] != '0':
            temp+=convertedN[i]
        elif temp :
            nums.append(int(temp))
            temp = ""
    if temp:
        nums.append(int(temp))
    if len(nums) == 1:
        for i in range(2,int(nums[0]**0.5)+1):
            if nums[0]% i == 0:
                return 0
        if nums[0] == 1:
            return 0
        return 1
    else:
        maxNum = max(nums)
        primes = [0]*(maxNum+1)
        primes[1] = 1
        for i in range(2, int(maxNum**0.5)+1):
            for j in range(i+i,maxNum+1,i):
                primes[j] = 1
        for num in nums:
            if not primes[num]:
                answer+=1
    return answer
print(solution(1,6))