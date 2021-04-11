#09 문자열 압축
def solution(s):
    check = []
    length = len(s)
    result = ""

    if length == 1:
        return 1

    for i in range(1, length//2 + 1):
        cnt = 1
        sliced_s = s[:i]
        for j in range(i, length, i):
            if s[j:j+i] == sliced_s:
                cnt+=1
            else:
                if cnt == 1:
                    cnt=""
                result +=str(cnt)+sliced_s
                sliced_s=s[j:j+i]
                cnt=1

        if cnt==1:
            cnt=""
        result += str(cnt)+sliced_s
        check.append(len(result))
        result = ""