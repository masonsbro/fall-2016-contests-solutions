from random import randint

def main():
    T = 15
    print(T)
    print("""5 5 140
1 2 20
2 3 20
3 4 20
4 2 20
4 5 20
2 0 50
3 2 100
1 2 20
2 3 20
4 4 1000000000
1 2 1
2 3 -1
3 4 -1
4 1 -1
4 4 1000000000
1 2 1
2 3 1
3 4 -1
4 1 -1
4 4 1000000000
1 2 1
2 3 1
3 4 -1
4 1 1
5 5 100
1 2 20
2 3 20
3 4 20
4 2 20
1 5 20
8 9 10010
1 2 20
2 3 -2
3 4 -4
4 2 -15
3 5 20
5 6 7
6 7 8
7 5 2
2 8 -5


""")

    for _ in range(8, T):
        n = randint(1, 150)
        m = randint(n - 1, n * (n - 1) // 2 - 5)
        s = randint(25 * n, int(1e18))
        used = set()
        print(n, m, s)
        for _ in range(m):
            u, v = randint(1, n), randint(1, n)
            while (u, v) in used:
                u, v = randint(1, n), randint(1, n)

            used.add((u, v))
            print(u, v, randint(-20, 20))

main()
