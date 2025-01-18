def length_sum(L:list[str]) -> int:
    if len(L) > 2:  #This is evaluated for the call for variable first
        result = len(L[0]) + len(L[1]) + len(L[2]) #the string length of the first three entries in the list are added
    elif len(L) > 1:    #This is evaluated for the call for variable third
        result = len(L[0]) + len(L[1])  #The string length of the two list entries are added
    elif len(L) > 0:    #This is evaluated for the call for variable second
        result = len(L[0])  #The string length of the one list entry is counted
    else:
        result = 0
    return result

first = length_sum(["this", "is", "the", "first", "call"])
second = length_sum(["second call"])
third = length_sum(["another", "call"])
print()

