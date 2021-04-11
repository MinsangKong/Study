#Q7 럭키 스트레이트
#import sys
#input = sys.stdin.readline
n = input().rstrip()
left = 0
right = 0
for i in range(len(n)):
    if i < len(n)//2:
        left+=int(n[i])
    else:
        right+=int(n[i])
if left==right:
    print("LUCKY")
else:
    print("READY")