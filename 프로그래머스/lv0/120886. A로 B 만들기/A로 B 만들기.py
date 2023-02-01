# before를 for문으로 하나씩 넣어봄
# in after를 통해 있는지 확인
# 2개이상의 문자열 체크 -> 확인한 i는 replace로 제거
# after에 문자열이 남아있으면 0 
def solution(before, after):
    answer = 0
    for i in before:
        if i in after:
            after = after.replace(i,'',1)
    if len(after) > 0:
        return 0
    else:
        return 1 