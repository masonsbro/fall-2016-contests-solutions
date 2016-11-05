import random

T = 20
min_N = 3
max_N = 1000

contest_in_name = 'contest.in'
contest_out_name = 'contest.out'

random.seed(123735829)

def random_seq(N):
    return [random.randint(1, N) for i in range(N - 2)]

def gen_tree(N, seq):
    degree = {i: 1 for i in range(1, N + 1)}
    for v in seq:
        degree[v] += 1
    edges = []
    for v in seq:
        for u in range(1, N + 1):
            if degree[u] == 1:
                edges.append((u, v))
                degree[u] -= 1
                degree[v] -= 1
                break
    last = []
    for u in range(1, N + 1):
        if degree[u] == 1:
            last.append(u)
            degree[u] -= 1
    assert len(last) == 2
    edges.append(tuple(last))
    random.shuffle(edges)
    return edges

contest_in = open(contest_in_name, 'w')
contest_out = open(contest_out_name, 'w')
contest_in.write(str(T) + '\n')
for t in range(T):
    N = random.randint(min_N, max_N)
    seq = random_seq(N)
    edges = gen_tree(N, seq)
    contest_in.write(str(N) + '\n')
    for edge in edges:
        contest_in.write(str(edge[0]) + ' ' + str(edge[1]) + '\n')
    contest_out.write(' '.join(map(str, seq)) + '\n')
contest_in.close()
contest_out.close()
