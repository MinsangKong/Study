#https://www.acmicpc.net/problem/2590
#백준 2590번 색종이(구현)
#import sys
#input=sys.stdin.readline
paper = [0, 0, 0, 0 ,0, 0]
for i in range(6):
    n = int(input())
    for j in range(n):
        paper[i] += ((i+1)*(i+1))

cnt = 0
while 1:
    if max(paper) == 0:
        break
    result = 36
    
    if paper[5] >= 36:
        cnt += 1
        paper[5] -= 36
        continue
        
    elif paper[4] >= 25:
        paper[4] -= 25
        cnt += 1
        for i in range(11):
            if paper[0] == 0:
                break
            paper[0] -= 1
        continue
            
    elif paper[3] >= 16:
        paper[3] -= 16
        cnt += 1
        result -= 16
        for i in range(5):
            if paper[1] == 0:
                break
            paper[1] -= 4
            result -= 4
        for i in range(20):
            if paper[0] == 0 or result == 0:
                break
            paper[0] -= 1
            result -= 1
        continue
        
    elif paper[2] >= 9:
        if paper[2] >= 36:
            paper[2] -= 36
            result -= 36
            cnt += 1
        elif paper[2] >= 27:
            cnt += 1
            paper[2] -= 27
            result -= 27
            if paper[1] >= 4:
                paper[1] -=4
                result -= 4
        elif paper[2] >= 18:
            cnt += 1
            paper[2] -= 18
            result -= 18
            for i in range(3):
                if paper[1] == 0 or result == 0:
                    break
                paper[1] -= 4
                result -= 4
        elif paper[2] >= 9:
            cnt += 1
            paper[2] -= 9
            result -= 9
            for i in range(5):
                if paper[1] == 0 or result == 0:
                    break
                paper[1] -=4
                result -= 4
        while 1:
            if paper[0] == 0  or result == 0:
                break
            paper[0] -= 1
            result -= 1
        continue
        
    elif paper[1] >= 4:
        cnt += 1
        for i in range(9):
            if paper[1] == 0:
                break
            result -= 4
            paper[1] -= 4
        while 1:
            if paper[0] == 0 or result == 0:
                break
            paper[0] -= 1
            result -= 1
        continue
        
    elif paper[0] >= 1:
        cnt += 1
        for i in range(36):
            if paper[0] == 0 or result == 0:
                break
            paper[0] -= 1
            result -= 1
        continue
print(cnt)
'''
구현 문제이긴 하지만 좀 독특한 방식의 구현 문제였다.
https://yhwan.tistory.com/20에서 설명하듯이 색종이가 들어갈 수 있는 공간을
미리 계산한 경우의 수를 if문으로 구현하면 되는 문제이다. 결국 어떻게 풀어야 할지 
몰라서 해설을 참고해서 풀었다...
'''