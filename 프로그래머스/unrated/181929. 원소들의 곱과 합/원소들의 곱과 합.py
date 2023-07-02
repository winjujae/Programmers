def solution(num_list):
    k = 1
    for i in range(len(num_list)) :
        k *= num_list[i]
    if k < sum(num_list)**2 :
        answer = 1
    elif k > sum(num_list)**2 :
        answer = 0
    return answer