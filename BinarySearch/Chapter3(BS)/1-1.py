#Q27 정렬된 배열에서 특정 수의 개수 구하기
#import sys
#input = sys.stdin.readline
import bisect

n, x = map(int, input().split())
nums = list(map(int, input().split()))

result = bisect.bisect_right(nums,x)-bisect.bisect_left(nums,x)
if result != 0:
    print(bisect.bisect_right(nums,x)-bisect.bisect_left(nums,x))
else:
    print(-1)