def solution(num_list):
    odd_str = ""
    even_str = ""
    for num in num_list:
        if num % 2 == 1:
            odd_str += str(num)
        else:
            even_str += str(num)
            
    odd_sum = int(odd_str) if odd_str else 0
    even_sum = int(even_str) if even_str else 0
    
    return odd_sum + even_sum