#https://www.acmicpc.net/problem/1475
#백준 1475번 방 번호(구현)
#import sys
#input = sys.stdin.readline
n = input()
num = [1,1,1,1,1,1,1,1,1,1]
cnt = 1
for i in n:
    if num[int(i)] > 0:
        num[int(i)]-=1
    else:
        if int(i) == 6 and num[9] > 0 :
            num[9]-=1
        elif int(i) == 9 and num[6] > 0 :
            num[6]-=1
        else:
            num=[x+1 for x in num]
            num[int(i)]-=1
            cnt+=1
print(cnt)