#https://www.acmicpc.net/problem/1748
#백준 1478번 수 이어 쓰기1(구현)
#import sys
#input = sys.stdin.readline
n = input().rstrip()
result = 0
if len(n) == 1 :
    result=int(n)
else:
    j=9
    k=1
    for i in range(len(n)-1,-1,-1):
        if i==0:
            cnt = int(n)-10**(len(n)-1)+1
            result+=len(n)*cnt
        else :
            result+=j*k
            k+=1
            j*=10
print(result)
'''
하나하나씩 계산하면 무조건 시간초과가 발생하기 때문에 점화식을 세워서 풀어야한다.
그런데 비효율적으로 점화식을 계산했다. 다른 사람이 푼 문제를 보니까 더 효율적이었다.
너무 자리수 하나하나에 집착해서 문제를 풀었다. 더 효율적인 방법이 있었는데 아쉽다.
'''