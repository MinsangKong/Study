#https://www.acmicpc.net/problem/20440
#백준 20440번 🎵니가 싫어 싫어 너무 싫어 싫어 오지 마 내게 찝쩍대지마🎵 - 1(누적합)
#import sys
#input = sys.stdin.readline

n = int(input())

counter = dict()

for _ in range(n):
    s, e = map(int, input().split())
    if s in counter:
        counter[s] += 1
    else:
        counter[s] = 1
    if e in counter:
        counter[e] -= 1
    else:
        counter[e] = -1
        
cntMax = 0
start, end = 0, 0
cur = 0

sorted_Counter = sorted(counter.keys())
for time in sorted_Counter:
    cur += counter[time]
    if cur > cntMax:
        cntMax = cur
        start = time
        
end = start
idx = sorted_Counter.index(start)
if idx+1 <= len(sorted_Counter):
    for i in range(idx+1, len(sorted_Counter)):
        end = sorted_Counter[i]
        if counter[sorted_Counter[i]] != 0:
            break

print(cntMax)
print(start, end)