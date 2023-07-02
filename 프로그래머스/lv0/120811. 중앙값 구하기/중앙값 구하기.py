def solution(array):
    array.sort()
    n = len(array)
    med = int((n+1)/2)-1
    answer = array[med]
    return answer