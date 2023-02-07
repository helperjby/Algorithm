def solution(array, n):
    answer = []
    array = sorted(array)
    for i in array:
        answer.append(abs(n-i))
    return array[answer.index(min(answer))]