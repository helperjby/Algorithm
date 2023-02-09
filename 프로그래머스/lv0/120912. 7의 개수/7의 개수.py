def solution(array):
    splited = []
    answer = 0
    for i in array:
        m = list(str(i))
        splited = splited + m

    for i in splited:
        if int(i) == 7:
            answer += 1

    return answer
