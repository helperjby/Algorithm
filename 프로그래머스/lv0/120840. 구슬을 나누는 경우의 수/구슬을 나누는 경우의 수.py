def solution(balls, share):
    balls_f = 1
    share_f = 1
    b_s_f = 1
    for i in range(1,balls+1):
        balls_f *= i
    for i in range(1,share+1):
        share_f *= i
    for i in range(1, balls-share+1):
        b_s_f *= i
    return balls_f / (b_s_f*share_f)
