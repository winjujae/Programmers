def solution(a, b):
    if a % 2 == 1 and b % 2 == 1:
        answer = a**2 + b**2
    elif a % 2 == 1 or b % 2 == 1:
        answer = (a + b) * 2
    else:
        answer = max(a, b) - min(a, b)
    return answer