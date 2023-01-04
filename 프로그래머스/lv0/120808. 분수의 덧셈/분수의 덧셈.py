def solution(denum1, num1, denum2, num2):
    sum_s = denum1 * num2 + denum2 * num1
    sum_m = num1 * num2
    x, y = sum_s, sum_m
    while y:
        x, y = y, x % y
    answer = [sum_s/x, sum_m/x]
    return answer