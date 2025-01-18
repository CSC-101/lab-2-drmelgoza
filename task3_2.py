def function2(a:int, b:int, c:int) -> int:
    if a > b and a < c:
        return a - b # evaluated completely when b < a and a < c.
    elif b > c:
        return b + c # evaluated completely when b >= a and a >= c and b > c
    else:
        return 2 * c # evaluated completely when b >= a and a >= c and b <= c

answer1 = function2(3, 2, 1) #the value of answer1 is 3
answer2 = function2(2, 3, 1) #the value of answer2 is 4
answer3 = function2(2, 1, 3) #the value of answer3 is 1
print()
