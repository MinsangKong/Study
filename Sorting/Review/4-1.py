#https://www.acmicpc.net/problem/11652
#백준 11652번 카드(정렬)
#import sys
#input = sys.stdin.readline

n = int(input())
num = []
for _ in range(n):
    num.append(int(input()))

num.sort()
count = 0
check1 = 1
check2 = 0
result = 0
for i in range(1,n):
    if num[i] == num[i-1]:
        check1+=1
    else:
        if check2 < check1:
            check2 = check1
            result = num[i-1]
        check1 = 1
if check2 < check1:
    print(num[-1])
else:
    print(result)
'''
문제 시간 제한이 빡빡하기 때문에 sort를 한 다음에 check를 하는 식으로 풀어야 한다.
count함수를 쓰면 시간 초과, 미리 배열을 만들어 놓으면 메모리 초과가 발생한다.
'''