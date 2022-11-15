def list_manipulation(lst, command, location, value=None):
    if command == 'remove':
        if location == 'beginning':
            return lst.pop(0)
        elif location == 'end':
            return lst.pop()
    elif command == 'add':
        if location == 'beginning':
            lst.insert(0, value)
            return lst
        elif location == 'end':
            lst.append(value)
            return lst


lst = [1, 2, 3]
print(f"{list_manipulation(lst, 'remove', 'end')} should be 3")
print(f"{list_manipulation(lst, 'remove', 'beginning')} should be 1")
print(f"{lst} should be [2]")

lst = [1, 2, 3]
print(
    f"{list_manipulation(lst, 'add', 'beginning', 20)} should be [20, 1, 2, 3]")
print(
    f"{list_manipulation(lst, 'add', 'end', 30)} should be [20, 1, 2, 3, 30]")
print(f"{lst} should be [20, 1, 2, 3, 30]")

print(f"{list_manipulation(lst, 'foo', 'end') is None} should be True")
print(f"{list_manipulation(lst, 'add', 'dunno') is None} should be True")
