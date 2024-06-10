def levenshtein_distance(token1, token2):
    m = len(token1) + 1
    n = len(token2) + 1

    D = [[0] * n for _ in range(m)]

    for i in range(m):
        D[i][0] = i
    for j in range(n):
        D[0][j] = j

    for i in range(1, m):
        for j in range(1, n):
            if token1[i-1] == token2[j-1]:
                cost = 0
            else:
                cost = 1

            D[i][j] = min(D[i-1][j]+1, D[i][j-1]+1, D[i-1][j-1]+cost)

    return D[m-1][n-1]

assert levenshtein_distance('hi', 'hello') == 4
print(levenshtein_distance('hola', 'hello'))