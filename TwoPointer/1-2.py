def is_palindrome(s):
    if s == s[::-1]:
        return True


def solution(s):
    if is_palindrome(s):
        return 0
    
    i = 0
    j = len(s) - 1

    while i < j:
        if s[i] != s[j]:
            if is_palindrome(s[i + 1: j + 1]):
                return 1
            elif is_palindrome(s[i: j]):
                return 1
            else:
                return 2
        i += 1
        j -= 1
        

n = int(input())
for _ in range(n):
    s = input().strip()
    print(solution(s))