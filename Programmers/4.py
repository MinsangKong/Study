#https://programmers.co.kr/learn/courses/30/lessons/42885
#level 2 구명보트(그리디)
def solution(people, limit):
    count = 0
    people.sort()
    """while len(people) > 0: #효율성 테스트에서 pop이나 del을 쓰면 테스트1에서 에러 발생
        if len(people) == 1:
            del people[0]
            return count + 1
        else: 
            if people[0] + people[-1] <= limit:
                del people[0]
                del people[-1]
            else:
                del people[-1]
            count += 1  """
    left = 0
    right = len(people)-1
    while right >= left: 
            weight = people[right]
            right-=1
            if weight + people[left] <= limit :
                left+=1
            count+=1
    return count