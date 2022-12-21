def solution(numbers):
    a = numbers
    a.sort(reverse=True)
    answer = a[0] * a[1]
    return answer