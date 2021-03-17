#chapter3 그리디 문자열 뒤집기
#import sys
#input = sys.stdin.readline
line = input()
cnt_0 = 0
cnt_1 = 0
check = 0
if line[0] == '0':
    check = 1
    cnt_1+=1
else :
    check = 0
    cnt_0+=1
    
for i in range(1,len(line)):
    if line[i] == '0' and check == 0:
        cnt_1+=1
        check = 1
    elif line[i] == '1' and check == 1 :
        cnt_0+=1
        check=0
print(min(cnt_1, cnt_0))