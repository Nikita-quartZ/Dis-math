def calculate(n: int, m: int, edges: list[tuple[int, int]]) -> tuple[set[bool], set[bool], set[bool]]:
    reflex, symm, transit = set(), set(), set()
    if n == 0:
        pass
    elif n < m:
        reflex.add(False)
        for edge in edges:
            if edge[0] == edge[1]:
                reflex.add(True)
                symm.add(True)
            else:
                if n > 2:
                    for f_edge in edges:
                        if edge[1] == f_edge[0] and edge[0] != f_edge[1] and f_edge[0] != f_edge[1]:
                            transit.add((edge[0], f_edge[1]) in edges)
                        if transit == {True, False}:
                            break
                symm.add((edge[1], edge[0]) in edges)

            if reflex == symm == transit == {True, False} or n <= 2 and reflex == symm == {True, False}:
                break
    elif n == m:
        for i in range(n):
            reflex.add((i + 1, i + 1) in edges)
            symm.add((edges[i][1], edges[i][0]) in edges)
            if n > 2 and edges[i][0] != edges[i][1]:
                for f_edge in edges:
                    if edges[i][1] == f_edge[0] and edges[i][0] != f_edge[1] and f_edge[0] != f_edge[1]:
                        transit.add((edges[i][0], f_edge[1]) in edges)
                    if transit == {True, False}:
                        break
            if reflex == symm == transit == {True, False} or n <= 2 and reflex == symm == {True, False}:
                break
    else:
        for i in range(1, m + 1):
            reflex.add((i, i) in edges)
            if reflex == {True, False}:
                break
        for edge in edges:
            symm.add((edge[1], edge[0]) in edges)
            if n > 2 and edge[0] != edge[1]:
                for f_edge in edges:
                    if edge[1] == f_edge[0] and edge[0] != f_edge[1] and f_edge[0] != f_edge[1]:
                        transit.add((edge[0], f_edge[1]) in edges)
                    if transit == {True, False}:
                        break
            if symm == transit == {True, False} or n <= 2 and symm == {True, False}:
                break
    return reflex, symm, transit


n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(n)]

reflex_list, symm_list, transit_list = calculate(n, m, edges)

# Проверяем рефлексивность
if all(reflex_list):
    print('Рефлексивное')
else:
    print('Не рефлексивное')

# Проверяем транзитивность
if all(transit_list):
    print('Транзитивное')
else:
    print('Не транзитивное')

# Проверяем симметричность
if all(symm_list):
    print('Симметричное')
else:
    print('Антисимметричное')
