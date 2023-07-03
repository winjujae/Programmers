def solution(myString, pat):
    myString = myString.replace('A','C')
    myString = myString.replace('B','D')
    myString = myString.replace('C','B')
    myString = myString.replace('D','A')
    if pat in myString :
        return 1
    else :
        return 0