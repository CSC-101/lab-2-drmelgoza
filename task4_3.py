def surprising(L:list[str], other:str) -> list[str]:
    L.append(other.upper())
    return L

words = ["this", "is", "confusing", "code."]
first = surprising(words, "Avoid")
second = surprising(words, "such")
    #words has a value of ["this", "is", "confusing", "code", "AVOID," "SUCH"]
    #first has the same value of words, and second has the same value of words as well.
    #as the list "words" was appended in the function, all variables that held the list "words" also changed to reflect the change in "words".

print()