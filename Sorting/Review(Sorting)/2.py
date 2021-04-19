#https://www.acmicpc.net/problem/11004
#백준 11004번 K번째 수(정렬)
#import sys
#input = sys.stdin.readline
n, k = map(int, input().split())
num = list(map(int, input().split()))
num.sort()
print(num[k-1])