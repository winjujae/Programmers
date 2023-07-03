def solution(s):
    s = s.lower()
    p, y = 0,0
    for char in s :
        if char == 'p' :
            p += 1
        elif char == 'y' :
            y += 1
    if p == y :
        answer = True
    else :
        answer = False
    return answer