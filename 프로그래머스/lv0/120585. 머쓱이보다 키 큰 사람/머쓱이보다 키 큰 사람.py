def solution(array, height):
    array.append(height)
    array.sort(reverse=True)
    a = array.index(height)
    return a