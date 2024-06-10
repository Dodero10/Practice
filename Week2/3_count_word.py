def count_word(file_path):
    counter = {}

    with open(file_path, 'r') as file:
        for line in file:
            words = line.split()
            for word in words:
                word.lower()
                if word in counter:
                    counter[word] += 1
                else:
                    counter[word] = 1

    return counter

file_path = "../P1_data.txt"
result = count_word(file_path)

assert result['who'] == 3

print(result['man'])