def max_kernel(num_list, k):
    res = []

    for i in range(0, len(num_list)-2):
        res.append(max(num_list[i:i+3]))
        print(num_list[i:i+3])

    return res

assert max_kernel ([3 , 4 , 5 , 1 , -44] , 3) == [5 , 5 , 5]
num_list = [3 , 4 , 5 , 1 , -44 , 5 ,10 , 12 ,33 , 1]
k = 3
print ( max_kernel ( num_list , k ) )

