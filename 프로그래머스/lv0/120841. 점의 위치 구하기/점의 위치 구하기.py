def solution(dot):
    a = dot[0]
    b = dot[1]
    c = []
    if a > 0 and b > 0:
        c.append(1)
    elif a > 0 and b < 0:
        c.append(4)
    elif a < 0 and b > 0:
        c.append(2)
    elif a < 0 and b < 0:
        c.append(3)
    return c[0]