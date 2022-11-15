def intersection(l1, l2):
    # return [val for val in l1 if val in l2]
    lst = []
    for item in l1:
        if item in l2:
            lst.append(item)
    return lst


print(f"{intersection([1, 2, 3], [2, 3, 4])} should be [2, 3]")
print(f"{intersection([1, 2, 3], [1, 2, 3, 4])} should be [1, 2, 3]")
print(f"{intersection([1, 2, 3], [3, 4])} should be [3]")
print(f"{intersection([1, 2, 3], [4, 5, 6])} should be []")
