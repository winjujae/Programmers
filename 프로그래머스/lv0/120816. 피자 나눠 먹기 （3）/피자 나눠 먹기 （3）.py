def solution(slice, n):
    if n <= slice :
        answer = 1
    elif n % slice == 0 :
        answer = n // slice
    else :
        answer = n // slice + 1
    return answer