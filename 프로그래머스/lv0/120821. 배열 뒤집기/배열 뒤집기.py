def solution(num_list):
    answer = []
    for i in range(len(num_list),0,-1):
        answer.append(num_list[i-1])
    return answer