def solution(n) :
    if n < 2:
        answer = 0
    else :
        answer = 0
        for num in range(2, n + 1, 2):
            answer += num
    
    return answer