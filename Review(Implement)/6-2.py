#import sys
#input = sys.stdin.readline
v = "aeiou"
while True:
    s = input()
    chk,chk2 = 0,0 #chk=같은 글자 연속, chk2 = 모음 여부 여부  
    if s == "end": break;
    for i in s:
        if i in v:
            chk2=1
            break
    for i in range(1,len(s)):
        if s[i] == s[i-1] and s[i] not in 'eo': 
            chk=1
            break
    for i in range(len(s)-2):
        if s[i] in v and s[i+1] in v and s[i+2] in v: 
            chk=1
            break
        elif s[i] not in v and s[i+1] not in v and s[i+2] not in v: 
            chk=1
            break

    if chk == 1 or chk2 == 0: 
        print("<" + s + "> is not acceptable." )
    else: 
        print("<" + s + "> is acceptable." )
'''
하나 하나 세지 않고 방식을 바꿔보니 정답으로 나왔다.
'''