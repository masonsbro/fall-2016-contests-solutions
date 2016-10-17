import random

random.seed(12345)

MAX_N = 700
MAX_S = 20
MAX_D = 700
MAX_Y = 20
MAX_H = 400

# 6 hardcoded

print """20
1 1 2 0
2
10
5 2 1 6
1 2
1 5
2 4
3 4
4 5
5 3
1 2 3 4 5
10 8
5 2 1 6
1 2
1 5
2 4
3 4
4 5
5 3
1 2 3 4 5
10 5
5 2 1 6
1 2
1 5
2 4
3 4
4 5
5 3
1 2 3 4 5
10 1
2 2 1 2
1 2
2 1
2 2
2 1
2 2 1 2
1 2
2 1
2 2
2 5"""

# big cases

# all businesses form a big cycle, best is 0
N = MAX_N
K = MAX_N
S = MAX_S
D = MAX_N
print N, K, S, D
for i in range(1, N + 1):
    print i, i + 1 if i + 1 <= N else 1
print " ".join([str(MAX_Y)]*N)
print " ".join([str(MAX_H - 1)]*K)

# all businesses form a big cycle, best is not 0
N = MAX_N
K = MAX_N
S = MAX_S
D = MAX_N
print N, K, S, D
for i in range(1, N + 1):
    print i, i + 1 if i + 1 <= N else 1
print " ".join([str(MAX_Y - 1)]*N)
print " ".join([str(MAX_H)]*K)

def gen_rand(N=None, K=None, S=None, D=None):
    if N is None: N = random.randint(MAX_N / 4, MAX_N)
    if K is None: K = random.randint(1, N)
    if S is None: S = random.randint(0, MAX_S)
    if D is None: D = random.randint(0, MAX_D)
    edges = set([(random.randint(1, N), random.randint(1, N)) for _ in range(D)])
    D = len(edges)
    Y = [random.randint(0, MAX_Y) for _ in range(N)]
    H = [random.randint(0, MAX_H) for _ in range(K)]
    print N, K, S, D
    if D > 0:
        print "\n".join(map(lambda x: "%d %d" % x, edges))
    print " ".join(map(str, Y))
    print " ".join(map(str, H))

# random

gen_rand(S=0)
gen_rand(D=0)

for i in range(10):
    gen_rand()
