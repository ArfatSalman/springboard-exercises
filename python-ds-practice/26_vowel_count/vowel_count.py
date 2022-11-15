def vowel_count(phrase):
    vowel_dict = {}
    for letter in phrase.lower():
        if letter in 'aeiou':
            vowel_dict[letter] = vowel_dict.get(letter, 0) + 1
    return vowel_dict


print(f"{vowel_count('rithm school')}")
print(f"{vowel_count('HOW ARE YOU? i am great!')}")
