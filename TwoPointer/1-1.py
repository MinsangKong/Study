#https://www.acmicpc.net/problem/17609
#백준 17609번 회문 (문자열)
#import sys
#input = sys.stdin.readline

def palindrome(word):
    for i in range(len(word)//2):
        if word[i] != word[len(word)-1-i]:
            return False
    return True

def semiPalin(l,r,state,word):
    s = l
    e = r
    check = state
    while s < e :
        if word[s] != word[e]:
            if check :
                check = False
                if word[s+1] == word[e] and semiPalin(s+1,e,check,word):
                    return True
                if word[s] == word[e-1] and semiPalin(s,e-1,check,word):
                    return True
                return False
            else:
                return False
        else:
            s += 1
            e -= 1
    return True

n = int(input())

for _ in range(n):
    word = input().rstrip()
    if palindrome(word):
        print(0)
    else:
        if semiPalin(0,len(word)-1,True,word):
            print(1)
        else:
            print(2)