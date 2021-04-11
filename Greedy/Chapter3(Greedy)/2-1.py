#chapter3 그리디 곱하기 혹은 더하기
#import sys
#input = sys.stdin.readline
arr = input()
result = 0

for i in arr:
    if result == 0:
        result = int(i)
    elif i == '0' or i == '1' or result <= 1:
        result+=int(i)
    else:
        result*=int(i)
        
print(result)