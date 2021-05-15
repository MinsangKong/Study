#chapter3 볼링공 고르기
#import sys
#input = sys.stdin.readline
n, m = map(int, input().split())
arr = list(map(int, input().split()))
count = 0

for i in range(n):
    for j in range(i+1, n):
        if arr[i] != arr[j]:
            count+=1
            
print(count)
'''
해설의 답이 2 중 for문을 사용하지 않기 때문에 시간적으로 더 효율적이다.
'''