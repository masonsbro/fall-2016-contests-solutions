import string
from random import choice, randint


def gen_word():
    return ''.join(choice(string.ascii_lowercase) for _ in range(4))


def main():
    T = randint(10, 12)
    print(T)
    print("""5 3
stick spray stick stick bat
1 1
hook
2 2
a a
10 4
a b c a d a b e f a
10 3
b a a a a a a a a c""")
    for _ in range(6, T - 2):
        n = randint(10000, 100000)
        k = randint(7, 20)
        chars = [choice(string.ascii_lowercase) for _ in range(n)]
        print(n, k)
        print(' '.join(chars))

    for _ in range(T - 2, T):
        n = randint(1000, 10000)
        k = randint(n // 10, n // 2)

        words = [gen_word() for _ in range(n)]
        print(n, k)
        print(' '.join(words))


main()
