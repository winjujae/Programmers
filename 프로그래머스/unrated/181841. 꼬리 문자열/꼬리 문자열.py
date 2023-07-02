def solution(str_list, ex):
    answer = ''
    for char in str_list :
        if not ex in char :
            answer += char
    return answer