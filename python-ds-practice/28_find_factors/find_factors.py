def find_factors(num):
    output = []
    for val in range(num):
        if num % (val+1) == 0:
            output.append(val+1)
    return output


print(find_factors(10))
print(find_factors(11))
print(find_factors(111))
print(find_factors(321421))
