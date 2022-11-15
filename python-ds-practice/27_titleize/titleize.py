def titleize(phrase):
    return phrase.title()
    # return ' '.join([val.capitalize() for val in phrase.split(' ')])


print(titleize('this is awesome'))
print(titleize('oNLy cAPITALIZe fIRSt'))
