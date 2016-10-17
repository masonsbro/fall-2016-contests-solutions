def main():
    m, n = map(int, input().split())
    assert(1 <= m <= 1000)
    assert(1 <= n <= 1000)
    ia = list(map(int, input().split()))
    assert(len(ia) == m + 1)
    a = list(input().split())
    assert(len(a) == ia[-1])
    ja = list(map(int, input().split()))
    assert(len(ja) == ia[-1])

    a_ptr = 0
    for row_ind in range(m):
        row = ['0'] * n
        num_in_row = ia[row_ind + 1] - ia[row_ind]
        for _ in range(num_in_row):
            row[ja[a_ptr]] = a[a_ptr]
            a_ptr += 1

        print(' '.join(row))

t = int(input())
for _ in range(t):
    main()
