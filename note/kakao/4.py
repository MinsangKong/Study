from collections import deque
def bfs(start,end,roads,traps):
    visited = []
    q = deque()
    trap_count = [0]*len(traps)
    q.append((start,0,trap_count))
    while q:
        s, dist, count = q.popleft()
        if s == end:
            return dist
        check = []
        for i in range(len(count)):
            if count[i] != 0:
                check.append(traps[i])
        for road in roads:
            if road[0] == s and [road[0],road[1]] not in visited and road[0] not in check:
                if road[1] in traps:
                    if count[traps.index(road[1])] == 0:
                        count[traps.index(road[1])] = 1
                    else:
                        count[traps.index(road[1])] = 0
                q.append((road[1],dist+road[2],count))
                visited.append([road[0],road[1]])
            elif road[0] == s and [road[0],road[1]] not in visited and road[0] in check:
                if (road[0] in traps and road[1] in traps)and(count[traps.index(road[1])] == 1 and count[traps.index(road[0])] == 1):
                    visited.append([road[0],road[1]])
                    if road[1] in traps:
                        if count[traps.index(road[1])] == 0:
                            count[traps.index(road[1])] = 1
                        else:
                            count[traps.index(road[1])] = 0
                    q.append((road[1],dist+road[2],count))
                    visited.append([road[0],road[1]])
            elif road[1] == s and [road[1],road[0]] not in visited and road[1] in check:
                if road[0] in traps:
                    if count[traps.index(road[0])] == 0:
                        count[traps.index(road[0])] = 1
                    else:
                        count[traps.index(road[1])] = 0
                visited.append([road[1],road[0]])
                q.append((road[0],dist+road[2],count))
            
            
def solution(n, start, end, roads, traps):
    return bfs(start,end,roads,traps)
print(solution(4, 1, 4, [[1, 2, 1], [3, 2, 1], [2, 4, 1]], [2, 3]))