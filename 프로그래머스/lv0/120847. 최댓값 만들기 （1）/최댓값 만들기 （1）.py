def solution(numbers):
    numbers.sort()
    answer = numbers[int(len(numbers))-1] * numbers[int(len(numbers))-2]
    return answer