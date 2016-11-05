import random

def gen_color():
    digits = 'ABCDEF01234789'

    return '#' + ''.join([random.choice(digits) for _ in range(6)])

T = 20
print(T)
print("""3 #FFFFFF
#ACDCDC
#EFFEFF
#DEADBF
2 #FFFFFF
#00FFFF
#FFFF00
2 #FFFFFF
#FFFF00
#00FFFF""")

for case in range(3, T):
    n = random.randint(1, 500 * case)
    print(n, gen_color())
    for _ in range(n):
        print(gen_color())
