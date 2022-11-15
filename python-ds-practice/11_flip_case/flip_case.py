def flip_case(phrase, to_swap):
    new_phrase = ''
    for letter in phrase:
        if letter.lower() == to_swap.lower():
            letter = letter.swapcase()
        new_phrase += letter
    return new_phrase


print(f"{flip_case('Aaaahhh', 'a')} should be aAAAhhh")
print(f"{flip_case('Aaaahhh', 'A')} should be aAAAhhh")
print(f"{flip_case('Aaaahhh', 'h')} should be AaaaHHH")
