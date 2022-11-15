def frequency(lst, search_term):
    return lst.count(search_term)


print(f"{frequency([1, 4, 3, 4, 4], 4)} should be 3")
print(f"{frequency([1, 4, 3], 7)} should be 0")
