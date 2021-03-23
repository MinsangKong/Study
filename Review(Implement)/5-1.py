#https://www.acmicpc.net/problem/2303
#백준 2303번 숫자게임(구현)
#import sys
#input = sys.stdin.readline
def sum_card(n):
    num = 0
    for i in range(len(n)-2):
        for j in range(i+1,len(n)-1):
            for k in range(j+1, len(n)):
                count = (n[i]+n[j]+n[k])%10
                if num < count:
                    num=count
    return num

n = int(input())
arr = []
result = []

for i in range(n):
    arr.append(list(map(int, input().split())))

for i in arr:
    rest = sum_card(i)
    result.append(rest)

print(max([ i for i, x in enumerate(result) if x == max(result) ])+1)