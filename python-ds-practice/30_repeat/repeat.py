def repeat(phrase, num):
    """Return phrase, repeated num times.

        >>> repeat('*', 3)
        '***'

        >>> repeat('abc', 2)
        'abcabc'

        >>> repeat('abc', 0)
        ''

    Ignore illegal values of num and return None:

        >>> repeat('abc', -1) is None
        True

        >>> repeat('abc', 'nope') is None
        True
    """
    result = ''
    if isinstance(num, int) and num >= 0:
        for i in range(num):
            result += phrase
        return result
    # if not isinstance(num, int) or num < 0:
    #     return None

    # return phrase * num


print(repeat('*', 3))
print(repeat('abc', 2))
print(repeat('abc', 0))
print(f"{repeat('abc', -1) is None}")
print(f"{repeat('abc', 'nope') is None}")
