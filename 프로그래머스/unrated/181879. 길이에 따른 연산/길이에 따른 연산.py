def solution(num_list):
    if len(num_list) >= 11 :
        answer = sum(num_list)
    elif len(num_list) < 11 :
        k = 1
        for i in range(len(num_list)) :
            k *= num_list[i]
        answer = k
    return answer