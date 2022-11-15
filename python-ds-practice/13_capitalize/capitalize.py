def capitalize(phrase):
    """Capitalize first letter of first word of phrase.

        >>> capitalize('python')
        'Python'

        >>> capitalize('only first word')
        'Only first word'
    """
    return phrase.capitalize()


print(f"{capitalize('python')} should be 'Python'")
print(f"{capitalize('only first word')} should be 'Only first word'")
