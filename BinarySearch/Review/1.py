#https://www.acmicpc.net/problem/2417
#백준 2417번 정수 제곱근(이분탐색)
#import sys
#input = sys.stdin.readline

n = int(input())

start = 0
end = n
result = 0
while start <= end:
    mid = (start+end)//2
    if mid**2 >= n:
        result = mid
        end = mid-1
    else:
        start = mid+1
        
print(result)