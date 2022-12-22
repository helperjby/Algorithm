def solution(money):
    answer = []
    aa = int(5500)
    answer.append(int(money/aa))
    answer.append(money%aa)
    return answer