def solution(my_string):
    k = ['a','e','i','o','u']
    answer = ''
    for char in my_string :
        if char not in k :
            answer += char
    return answer