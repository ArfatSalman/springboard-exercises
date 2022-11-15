def last_element(lst):
    if lst:
        return lst[-1]


print(f"{last_element([1,2,3])} should be 3")
print(f"{last_element([])} should be None")
