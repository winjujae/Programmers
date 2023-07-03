def solution(strArr):
    answer = []
    for i in range(len(strArr)):
        if i % 2 == 0:
            a = strArr[i].lower()
        else:
            a = strArr[i].upper()
        answer.append(a)
    return answer