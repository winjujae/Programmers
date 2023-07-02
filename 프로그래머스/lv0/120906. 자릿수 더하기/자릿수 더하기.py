def solution(n):
    answer = 0
    for i in range(len(str(n))) :
        answer += n // (10**i) % 10
    return answer