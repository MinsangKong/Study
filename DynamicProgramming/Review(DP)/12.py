#https://www.acmicpc.net/problem/1912
#백준 1912번 연속합(DP)
#import sys
#input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
    
if max(nums) <= 0:
    print(max(nums))
else:
    last = 0
    check = 0
    for i in nums:
        if i >= 0 :
            check+=i
        else:
            if check > last:
                last = check
            if check + i > 0 :
                check += i
            else:
                if check > last :
                    last = check 
                check = 0
    print(max(last,check))