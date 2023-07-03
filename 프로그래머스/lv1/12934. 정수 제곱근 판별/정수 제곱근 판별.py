def solution(n):
    x = range(1,n+1)
    for i in x :
        if i**2 == n :
            answer = int((i+1)**2)
            return answer
    answer = -1
    return answer