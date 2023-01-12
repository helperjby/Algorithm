def solution(emergency):
    rank = sorted(emergency, reverse=True)
    answer = []
    for i in emergency:
        answer.append(rank.index(i)+1)
    return answer