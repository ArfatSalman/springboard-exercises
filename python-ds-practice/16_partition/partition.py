def partition(lst, fn):
    # return [[val for val in lst if fn(val)], [val for val in lst if fn(val) == False]]
    true_list = []
    false_list = []

    for val in lst:
        if fn(val):
            true_list.append(val)
        else:
            false_list.append(val)

    return [true_list, false_list]


def is_even(num):
    return num % 2 == 0


def is_string(el):
    return isinstance(el, str)


strlst = ["hi", None, 6, "bye"]
print(f"{partition([1, 2, 3, 4], is_even)} should be [[2, 4], [1, 3]]")
print(f"{partition(strlst, is_string)} should be [['hi', 'bye'], [None, 6]]")
