N = int(input())

temp = []

while True:
    arrs = list(map(int, input().split()))
    if arrs[0] == -1 and arrs[1] == -1:
        break
    temp.append(arrs)

G = [[] for i in range(N + 1)]


for i in range(len(temp)):
    s, e = temp[i][0], temp[i][1]
    G[s].append(e)
    G[e].append(s)



visit = [0 for i in range(N+1)]


def bfs(v):
    Q=[]
    Q.append(v)
    visit[v] = 1
    while Q:
        v = Q.pop(0)
        for w in G[v]:
            if visit[w] == 0:
                Q.append(w)
                visit[w] = visit[v] + 1


score = []
people = []
mins = N
for i in range(1, N+1):
    visit = [0 for i in range(N + 1)]
    bfs(i)
    s = max(visit) - 1
    score.append(s)
    if mins > s:
        people = [i]
        count = 1
        mins = s
    elif mins == s:
        count += 1
        people.append(i)



print('{} {}'.format(mins, len(people)))
for i in people:
    print(i, end=' ')