def two_list_dictionary(keys, values):
    """Given keys and values, make dictionary of those.

        >>> two_list_dictionary(['x', 'y', 'z'], [9, 8, 7])
        {'x': 9, 'y': 8, 'z': 7}

    If there are fewer values than keys, remaining keys should have value
    of None:

        >>> two_list_dictionary(['a', 'b', 'c', 'd'], [1, 2, 3])
        {'a': 1, 'b': 2, 'c': 3, 'd': None}

    If there are fewer keys, ignore remaining values:

        >>> two_list_dictionary(['a', 'b', 'c'], [1, 2, 3, 4])
        {'a': 1, 'b': 2, 'c': 3}
   """
    two_list_dict = {}
    for key in range(len(keys)):
        if key < len(values):
            two_list_dict[keys[key]] = values[key]
        else:
            two_list_dict[keys[key]] = None
    return two_list_dict
    # out = {}

    # for idx, val in enumerate(keys):
    #     out[val] = values[idx] if idx < len(values) else None

    # return out


print(two_list_dictionary(['x', 'y', 'z'], [9, 8, 7]))
print(two_list_dictionary(['a', 'b', 'c', 'd'], [1, 2, 3]))
print(two_list_dictionary(['a', 'b', 'c'], [1, 2, 3, 4]))
