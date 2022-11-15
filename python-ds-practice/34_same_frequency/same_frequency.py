def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?

        >>> same_frequency(551122, 221515)
        True

        >>> same_frequency(321142, 3212215)
        False

        >>> same_frequency(1212, 2211)
        True
    """
    str1 = str(num1)
    str2 = str(num2)
    for num in str1:
        if str1.count(num) is not str2.count(num) or len(str1) != len(str2):
            return False
    return True


print(same_frequency(551122, 221515))
print(same_frequency(321142, 3212215))
print(same_frequency(1212, 2211))
print(same_frequency(1212, 22113434))

# def freq_counter(coll):
#     """Returns frequency counter mapping of coll."""

#     counts = {}

#     for x in coll:
#         counts[x] = counts.get(x, 0) + 1

#     return counts


# def same_frequency(num1, num2):
#     """Do these nums have same frequencies of digits?

#         >>> same_frequency(551122, 221515)
#         True

#         >>> same_frequency(321142, 3212215)
#         False

#         >>> same_frequency(1212, 2211)
#         True
#     """

#     return freq_counter(str(num1)) == freq_counter(str(num2))
