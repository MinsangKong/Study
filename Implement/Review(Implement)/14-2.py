#https://www.acmicpc.net/problem/2590
#백준 2590번 색종이(구현)
paper = [0] + [int(input()) for x in range(6)]
cnt = [0 for x in range(7)]

tot = paper[6]

tot += paper[5]
cnt[1] += paper[5] * 11

tot += paper[4]
cnt[2] += paper[4] * 5

tot += paper[3] // 4
rem = paper[3] % 4

if rem:
    tot += 1
    cnt[2] += 5 - (rem-1)*2
    cnt[1] += 7 - (rem-1)

paper[2] -= cnt[2]

if paper[2] < 0:
    cnt[1] += -paper[2] * 4
    paper[2] = 0

tot += paper[2] // 9
rem = paper[2] % 9

if rem:
    tot += 1
    cnt[1] += 36 - rem*4

paper[1] -= cnt[1]

if paper[1] < 0:
    paper[1] = 0

tot += paper[1] // 36
rem = paper[1] % 36

if rem:
    tot += 1

print(tot)
'''
다른 사람이 푼 방식은 대다수가 점화식으로 경우의 수를 구한 다음에 그 경우의 수에
맞게 코드를 작성해서 답을 얻었다. 결과적으로 나보다 실행속도도 빠르고 코드 수도 
적었다.
'''