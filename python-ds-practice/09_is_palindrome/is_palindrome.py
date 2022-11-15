def is_palindrome(phrase):
    real_phrase = phrase.lower().replace(' ', '')
    return real_phrase == real_phrase[::-1]


print(f"{is_palindrome('tacocat')} should be True")
print(f"{is_palindrome('noon')} should be True")
print(f"{is_palindrome('robert')} should be False")
print(f"{is_palindrome('taco cat')} should be True")
print(f"{is_palindrome('Noon')} should be True")
