def solution(s):
    a = list(s.lower())
    if a.count('p') != a.count('y') :
        return False
    else:
        return True

