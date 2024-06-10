def adjust_values_within_range(data, max_val, min_val):
    result = []
    for i in data:
        if i < min_val:
            result.append(min_val)
        elif i > max_val:
            result.append(max_val)
        else:
            result.append(i)
    return result

my_list = [5, 2, 5, 0, 1]
max_val = 1
min_val = 0
assert adjust_values_within_range(data=my_list, max_val=max_val, min_val=min_val) == [1, 1, 1, 0, 1]

my_list = [10, 2, 5, 0, 1]
max_val = 2
min_val = 1
print(adjust_values_within_range(data=my_list, max_val=max_val, min_val=min_val))