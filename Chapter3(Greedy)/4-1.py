#chapter3 만들 수 없는 금액
#import sys
#input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))

arr.sort()

cost = 1

for i in arr:
    if cost >= i:
        cost+=i
    else:
        break
        
print(cost)