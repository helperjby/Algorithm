def solution(hp):
    g,s,w = 5,3,1
    g_c = hp//g
    s_c = (hp%g)//s
    w_c = ((hp%g)%s)//w
    answer = g_c+s_c+w_c
    return answer