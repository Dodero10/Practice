def check_the_number(N):
    list_of_numbers = []
    result = ""
    for i in range(1, 5):
        # Thêm i vào list_of_numbers
        list_of_numbers.append(i)

    if N in list_of_numbers:
        result = "True"
    else:
        result = "False"

    return result

assert check_the_number(7) == "False"

N = 2
print(check_the_number(N))