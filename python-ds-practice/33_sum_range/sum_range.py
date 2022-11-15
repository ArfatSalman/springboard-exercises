def sum_range(nums, start=0, end=None):
    """Return sum of numbers from start...end.

    - start: where to start (if not provided, start at list start)
    - end: where to stop (include this index) (if not provided, go through end)

        >>> nums = [1, 2, 3, 4]

        >>> sum_range(nums)
        10

        >>> sum_range(nums, 1)
        9

        >>> sum_range(nums, end=2)
        6

        >>> sum_range(nums, 1, 3)
        9

    If end is after end of list, just go to end of list:

        >>> sum_range(nums, 1, 99)
        9
    """
    out = 0
    if end is not None:
        end += 1
    for i in nums[start:end]:
        out += i
    return out
    # if end is None:
    #     end = len(nums)

    # return sum(nums[start:end + 1])


numz = [1, 2, 3, 4]
print(sum_range(numz))
print(sum_range(numz, 1))
print(sum_range(numz, end=2))
print(sum_range(numz, 1, 3))
print(sum_range(numz, 1, 99))
