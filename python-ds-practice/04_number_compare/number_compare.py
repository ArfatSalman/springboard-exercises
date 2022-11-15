def number_compare(a, b):
    """Report on whether a>b, b>a, or b==a

        >>> number_compare(1, 1)
        'Numbers are equal'

        >>> number_compare(-1, 1)
        'Second is greater'

        >>> number_compare(1, -2)
        'First is greater'
    """
    if a > b:
        return "First is greater"
    if b > a:
        return "Second is greater"
    return "Numbers are equal"


print(f"{number_compare(1, 1)} should be Numbers are equal")
print(f"{number_compare(-1, 1)} should be Second is greater")
print(f"{number_compare(1, -2)} should be First is greater")
