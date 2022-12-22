def solution(n):
    if n < 8:
        return 1
    elif n > 7 and n%7 > 0:
        return int((n/7)+1)
    else:
        return int(n/7)
    return answer