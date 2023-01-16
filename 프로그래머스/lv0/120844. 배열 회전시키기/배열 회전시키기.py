def solution(numbers, direction):
    answer = []
    if direction == 'right':
        answer.append(numbers[-1])
        for i in numbers:
            answer.append(i)
        answer = answer[:-1]
    if direction == 'left':
        for i in range(1, (len(numbers))):
            answer.append(numbers[i])
        answer.append(numbers[0])
    return answer

# 디렉션 right인 경우
# -1번을 제외한 나머지 요소들 +1
# -1번은 0으로 스와프
# 디렉션 left인 경우
# 0번을 제외한 나머지 요소들 -1
# 0번은 -1로 스와프