def calculate_average(list_nums):
    if not list_nums:
        return None
    var = 0
    for i in list_nums:
        var += i
    return var / len(list_nums)

assert calculate_average([4, 6, 8]) == 6

print(calculate_average([4, 6, 8]))