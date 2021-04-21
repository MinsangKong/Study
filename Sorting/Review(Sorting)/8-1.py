#https://www.acmicpc.net/problem/18870
#백준 18870번 좌표 압축(정렬)
#import sys
#input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
check = sorted(set(arr))
dic = {check[i] : i for i in range(len(check))}
for i in arr:
    print(dic[i], end=' ')
