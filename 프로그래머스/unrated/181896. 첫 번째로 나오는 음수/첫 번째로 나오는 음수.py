def solution(num_list):
    count = 0
    for i in num_list :
        if i >= 0 :
            count += 1
        else :
            return count
    return -1