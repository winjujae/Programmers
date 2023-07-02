def solution(my_string):
    answer = []
    for char in my_string:
        if char.isdigit(): # 문자열이 숫자인가?
            answer.append(int(char))
    return sum(answer)