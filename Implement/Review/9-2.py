#https://www.acmicpc.net/problem/1748
#백준 1478번 수 이어 쓰기1(구현)
#import sys
#input = sys.stdin.readline
n = int(input())
ans, i = 0, 1
while i <= n:
    ans += (n-i+1)
    print(ans)
    i *= 10
print(ans)