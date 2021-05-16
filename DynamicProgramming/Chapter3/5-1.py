#Q35 못생긴 수

n = int(input())
dp = []
dp.append(1)
dp.append(2)
dp.append(3)
dp.append(4)
dp.append(5)
idx = 1
while len(dp) < n :
    new = set()
    for i in range(idx,len(dp)):
        for j in range(1,len(dp)):
            num = dp[i]*dp[j]
            if num not in dp :
                new.add(num)
    idx = len(dp)
    dp+=new
dp.sort()
print(dp)
print(dp[n-1])
'''
답 자체는 맞지만 dp 활용을 못해서 시간 면에서 훨씬 비효율적이다.
'''