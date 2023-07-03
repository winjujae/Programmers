def solution(n):
    k = str(n)
    a = []
    for i in k :
        a.append(int(i))
    answer = list(a[::-1])
    return answer