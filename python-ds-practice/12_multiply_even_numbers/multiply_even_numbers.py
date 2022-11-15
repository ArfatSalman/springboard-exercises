def multiply_even_numbers(nums):
    output = 1
    for num in nums:
        if num % 2 == 0:
            output *= num
    return output


print(f"{multiply_even_numbers([2, 3, 4, 5, 6])} should be 48")
print(f"{multiply_even_numbers([3, 4, 5])} should be 4")
print(f"{multiply_even_numbers([1, 3, 5])} should be 1")
