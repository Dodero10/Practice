def contains_number(integers, number=1):
    return any(i == number for i in integers)

my_list = [1, 3, 9, 4]
assert contains_number(my_list, -1) == False

my_list = [1, 2, 3, 4]
print(contains_number(my_list, 2))
