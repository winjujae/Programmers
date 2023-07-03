def solution(arr1, arr2):
    if len(arr1) > len(arr2):
        answer = 1
    elif len(arr1) < len(arr2):
        answer = -1
    else:
        sum1 = sum(arr1)
        sum2 = sum(arr2)
        if sum1 == sum2:
            answer = 0
        elif sum1 > sum2:
            answer = 1
        else:
            answer = -1
    return answer