def multiple_letter_count(phrase):
    letter_dict = {}
    for letter in phrase:
        letter_dict[letter] = letter_dict.get(letter, 0) + 1
    return letter_dict


print(f"{multiple_letter_count('yay')} should be 'y': 2, 'a': 1 with curly brackets")
print(f"{multiple_letter_count('Yay')} should be 'Y': 1, 'a': 1, 'y': 1 with curly brackets")
