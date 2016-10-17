from random import randint


def gen_mat(m, n):
    matrix = [[0 for _ in range(n)] for _ in range(m)]
    nnz = randint(1, (m * (n - 1) - 1) // 2)

    for _ in range(nnz):
        x, y, v = randint(0, m - 1), randint(0, n - 1), randint(1, 1000)
        matrix[x][y] = v

    return matrix


def compress(matrix):
    i = [0]
    a = []
    j = []
    count = 0
    for row in matrix:
        for ind, val in enumerate(row):
            if val != 0:
                count += 1
                a.append(val)
                j.append(ind)

        i.append(count)

    return a, i, j


def main():
    T = randint(1, 10)
    print(T)
    print("""4 4
0 0 2 3 4
5 8 3 6
0 1 2 1
4 6
0 2 4 7 8
1 2 3 4 5 6 7 8
0 1 1 3 2 3 4 5
2 2
0 2 4
1 1 1 1
0 1 0 1
5 5
0 0 0 0 0 0


1 10
0 5
1 2 3 4 5
0 2 4 6 8
10 1
0 0 1 1 2 2 3 3 4 4 5
1 2 3 4 5
0 0 0 0 0""")
    #a, i, j = compress([[0, 0, 0, 0], [5, 8, 0, 0], [0, 0, 3, 0], [0, 6, 0, 0]])
    #a, i, j = compress([[10, 20, 0, 0, 0, 0], [0, 30, 0, 40, 0, 0], [0, 0, 50, 60, 70, 0], [0, 0, 0, 0, 0, 80]])
    for _ in range(6, T):
        m, n = randint(3, 1000), randint(3, 1000)
        matrix = gen_mat(m, n)
        a, i, j = compress(matrix)
        print(m, n)
        print(' '.join(str(x) for x in i))
        print(' '.join(str(x) for x in a))
        print(' '.join(str(x) for x in j))


main()
