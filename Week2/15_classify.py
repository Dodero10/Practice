def function_helper(x):
    return 'T' if x > 0 else 'N'

def classify_numbers(data):
    res = [function_helper(x) for x in data]
    return res

data = [10, 0, -10, -1]
assert classify_numbers(data) == ['T', 'N', 'N', 'N']

data = [2, 3, 5, -1]
print(classify_numbers(data))
