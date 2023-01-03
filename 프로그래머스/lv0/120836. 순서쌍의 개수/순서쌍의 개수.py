def solution(n):
    answer = 0
    for i in range(1, n+1):
        if n%i == 0:
            answer += 1
    return answer



# n의 범위만큼 숫자를 하나씩 넣어봄
# n을 i로 나누었을 때 나머지가 없는 경우를 리스트에 담음
