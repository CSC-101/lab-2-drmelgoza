def smallest(n:float, m:float) -> float:
    if n < m:
        return n    #For neither first nor second is this evaluated
    else:
        return m

first = smallest(3, 2) #first is equal to 2
second = smallest(2, 2) #second is equal to 2.
#This not a reasonable result, since the two variables are equal to each other.
print()