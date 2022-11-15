def list_check(lst):
    """Are all items in lst a list?

        >>> list_check([[1], [2, 3]])
        True

        >>> list_check([[1], "nope"])
        False
    """
    for item in lst:
        if not isinstance(item, list):
            return False
    return True


lst_check1 = [[1], [2, 3]]
lst_check2 = [[1], "nope"]
print(f"{list_check(lst_check1)} should be True")
print(f"{list_check(lst_check2)} should be False")
