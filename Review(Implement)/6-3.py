def Take(L):
    def jo1(L):
        for i in L:
            if i in 'aeiou': return True
        return False
    def jo2(L):
        try:
            ppv,pv=False,False
            if L[0] in 'aeiou': ppv=True
            if L[1] in 'aeiou': pv=True
            for i in range(2,len(L)):
                now=False
                if L[i] in 'aeiou': now=True
                if ppv==pv==now: return False
                ppv=pv
                pv=now
            return True
        except:
            return True
    def jo3(L):
        for i in range(len(L)-1):
            if L[i]==L[i+1]:
                if not (L[i]=='e' or L[i]=='o'): return False
        return True
    return jo1(L) and jo2(L) and jo3(L)
st=input()
while st!='end':
    if Take(st):
        print('<%s> is acceptable.'%st)
    else:
        print('<%s> is not acceptable.'%st)
    st=input()
'''
가장 빠르게 실행되는 code를 보니까 조건을 함수로 만들어서 처리하니까 더 빠르게 나왔다
'''