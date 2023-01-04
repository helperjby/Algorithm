def solution(hp):
    g,s,w = 5,3,1
    answer = (hp//g) + ((hp%g)//s) + (((hp%g)%s)//w)
    return answer