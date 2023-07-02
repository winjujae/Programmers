def solution(n, k):
    if n < 10 :
        answer = 12000 * n + 2000 * k
    else :
        a = n // 10
        answer = 12000 * n + 2000 * (k-a)
    return answer