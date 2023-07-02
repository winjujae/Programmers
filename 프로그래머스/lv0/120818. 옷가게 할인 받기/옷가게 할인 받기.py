def solution(price):
    if price < 100000:
        discount = 0
    elif price < 300000 :
        discount = 0.05
    elif price < 500000:
        discount = 0.1
    else :
        discount = 0.2
    answer = int(price - (price * discount))
    return answer