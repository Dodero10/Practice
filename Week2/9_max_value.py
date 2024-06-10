def max_value(lst):
    if not lst:
        return None
    max_value = lst[0]
    for num in lst:
        if num > max_value:
            max_value = num
    return max_value

my_list = [1001, 9, 100, 0]
assert max_value(my_list) == 1001

my_list = [1, 9, 9, 0]
print(max_value(my_list))
