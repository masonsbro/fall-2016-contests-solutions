def bf(edges, most, reach, N):
    for rnd in range(N - 1):
        for u, v, w in edges:
            if reach[u]:
                if not reach[v]:
                    reach[v] = True
                    most[v] = most[u] + w
                else:
                    most[v] = max(most[v], most[u] + w)
    return most[N] if N in most else 0

T = int(raw_input())

for t in range(T):
    N, M, S = map(int, raw_input().split())
    edges = []
    for m in range(M):
        U, V, W = map(int, raw_input().split())
        edges.append((U, V, W))
    most = {}
    reach = {i: False for i in range(1, N + 1)}
    most[1] = 0
    reach[1] = True
    first = bf(edges, most, reach, N)
    second = bf(edges, most, reach, N)
    if second > first or first >= S:
        print "YES"
    else:
        print "NO"
