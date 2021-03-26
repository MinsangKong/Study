#08 문자열 재정렬
#import sys
#input = sys.stdin.readline
s =input().rstrip()
num = 0
string = []
for i in s:
    if '0' <= i <= '9':
        num+=int(i)
    else:
        string.append(i)
string.sort()
if num != 0:
    string.append(str(num))
print(''.join(string))