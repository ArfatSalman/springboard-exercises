def compact(lst):
    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """
    lst2 = []
    for item in lst:
        if item:
            lst2.append(item)
    return lst2
    # return [val for val in lst if val]


print(
    f"{compact([0, 1, 2, '', [], False, (), None, 'All done'])} should be [1, 2, 'All done']")
