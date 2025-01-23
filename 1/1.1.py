def polynom(n, table):
    coef = [row[-1] for row in table]
    
    for i in range(2 ** n):
        for j in range(i):
            if (i & j) == j:
                coef[i] ^= coef[j]
    
    terms = []
    for i in range(2 ** n):
        if coef[i] == 1:
            term = []
            for j in range(n):
                if (i & (1 << j)) != 0:
                    term.append(f'a{j + 1}')
            terms.append(''.join(term) if term else '1')
    return ' + '.join(terms)

n = 2
table = [
    [0, 0, 0],
    [0, 0, 1],
    [0, 0, 1],
    [0, 0, 1]
]

print(polynom(n, table))
