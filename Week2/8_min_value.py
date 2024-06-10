def min_value(lst):
    if not lst:
        return None
    min_value = lst[0]
    for num in lst:
        if num < min_value:
            min_value = num
    return min_value

my_list = [1, 22, 93, -100]
assert min_value(my_list) == -100

my_list = [1, 2, 3, -1]
print(min_value(my_list))
