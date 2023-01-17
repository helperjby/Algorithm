def solution(n):
    answer = []
    for i in range(1, n+1):
        if n%i == 0:
            answer.append(i)
    return answer


# n이 주어지면
# 1부터 n까지 차례로 넣어보면서 나누고 나머지가 0인 수들을 append