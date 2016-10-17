import copy

INF = int(1e9)


def bfs(graph, source, sink):
    q = [source]
    visited = set()
    prev = [None for _ in range(sink + 1)]
    while q:
        top = q[0]
        q = q[1:]
        visited.add(top)

        for succ in range(sink + 1):
            if graph[top][succ] > 0 and succ not in visited:
                prev[succ] = top
                q.append(succ)

    return None if prev[sink] is None else prev


def max_flow(cap, source, sink):
    residual = copy.deepcopy(cap)
    ans = 0
    while True:
        prev = bfs(residual, source, sink)
        if not prev:
            break

        min_edge = 1e10
        node = sink
        while node != source:
            min_edge = min(min_edge, residual[prev[node]][node])
            node = prev[node]

        ans += min_edge
        node = sink
        while node != source:
            residual[prev[node]][node] -= min_edge
            residual[node][prev[node]] += min_edge

            node = prev[node]

    return ans


def main():
    n, k, s, d = map(int, input().split())
    assert(1 <= k <= 700)
    assert(1 <= n <= 700)
    assert(k <= n)
    assert(0 <= s <= 20)
    assert(0 <= d <= 700)
    cap = [[0 for _ in range(n + 2)] for _ in range(n + 2)]
    for _ in range(d):
        u, v = map(int, input().split())
        assert(1 <= u <= n)
        assert(1 <= v <= n)
        u -= 1
        v -= 1
        cap[u][v] = INF

    y = list(map(int, input().split()))
    for yi in y:
        assert(0 <= yi <= 20)
    h = list(map(int, input().split()))
    for hi in h:
        assert(0 <= hi <= 400)

    assert(len(y) == n)
    assert(len(h) == k)
    w = [(-s * y[i] + h[i]) if i < k else (-s * y[i]) for i in range(n)]

    # assign every node to either source or sink
    source = n
    sink = n + 1
    all_pos = 0
    for i, weight in enumerate(w):
        if weight <= 0:
            cap[i][sink] = -weight
        else:
            cap[source][i] = weight
            all_pos += weight

    ans = max_flow(cap, source, sink)

    print(all_pos - ans)


T = int(input())
assert(1 <= T <= 20)
for _ in range(T):
    main()
