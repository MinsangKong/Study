#Q18 괄호 변환
def check(p):
    arr = []
    for i in p:
        if i == ')':
            if arr:
                j = arr.pop()
                if j != '(':
                    return False
            else:
                return False
        else:
            arr.append(i)
    return True
def dfs(p):
    if check(p):
        return p
    else:
        u = ""
        v = ""
        for i in range(len(p)):
            u+=p[i]
            if u.count('(') == u.count(')'):
                v = p[i+1:]
                if check(u):
                    return u+dfs(v)
                else:
                    n = ""
                    for i in u[1:-1]:
                        if i == ')':
                            n+='('
                        else:
                            n+=')'
                    return '('+dfs(v)+')'+n   
    
def solution(p):
    return dfs(p)
'''
type error가 발생해서 생각보다 오래 걸렸다. 구현 문제를 조금 꽈서 나오면 푸는데
너무 오래 걸리는 것 같다. 아직 이부분이 미숙하다. check는 다시 생각해보니까 굳이 비교를
안해도 pop을 할 수 없으면 숫자가 맞지 않다는 뜻이기 때문에 if j != '()' code는 필요 
없던 것 같다.
'''