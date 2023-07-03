def solution(n):
    x = range(1,n)
    k = []
    for i in x :
        if n % i == 1 :
            k.append(i)
    answer = min(k)
    return answer