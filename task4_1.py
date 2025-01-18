from typing import Optional

def checked_access(L:list[int], idx:int) -> Optional[int]:
    test = idx >= 0 and idx < len(L) # test has value False on first and value True on second
    if test:  # this check prevents an IndexError by only returning a value if the index is valid for the given list
        return L[idx]
    else:
        return None

first = checked_access([1, 0, 1], 9) #the value of first is None
second = checked_access([1, 0, 1], 2) #the value of second is 1
print()

