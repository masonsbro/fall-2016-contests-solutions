import random

random.seed(23589235)

T = 10
MAX_N = 300
MAX_B = 75

print T
for t in range(T):
    N = random.randint(1, MAX_N)
    B = [random.randint(1, MAX_B) for _ in range(N)]
    print N
    print " ".join(map(str, B))
