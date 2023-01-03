def solution(s1, s2):
    answer = 0
    for i in s2:
        answer += s1.count(i)
    return answer