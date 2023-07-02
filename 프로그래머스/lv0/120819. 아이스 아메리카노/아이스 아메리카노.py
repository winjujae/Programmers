def solution(money):
    can = money // 5500
    cant = money % 5500
    answer = [can, cant]
    return answer