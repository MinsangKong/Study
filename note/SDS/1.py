#문제_1: 낙타 옮기기 (Moving Camels)
#import sys
#input = sys.stdin.readline
def check(nums):
    if len(nums) == 3:
        return sum(nums)
    elif len(nums) == 4:
        return min(nums[0]+sum(nums), nums[0]+3*nums[1]+nums[3])
    else:
        return min(nums[len(nums)-1]+nums[0]+check(nums[:len(nums)-1]), nums[len(nums)-1]+nums[0]+2*nums[1]+check(nums[:len(nums)-2]))
def main():
    # 이곳에 소스코드를 작성하세요.
    # Python3 만 지원됩니다.
    # pass는 삭제해도 됩니다.
    idx = 1
    t = int(input())
    for _ in range(t):
        n = int(input())
        nums = list(map(int, input().split()))
        nums.sort()
        left = []
        result = 0
        if n <= 2:
            result = nums[-1]
        else :
            result = check(nums)
            
        print("#%d %d" % (idx, result))
        idx+=1
        
    
    
main()