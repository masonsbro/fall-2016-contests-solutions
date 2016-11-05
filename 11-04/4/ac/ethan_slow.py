T = int(raw_input())

for t in range(T):
    N = int(raw_input())
    adj = {i: set() for i in range(1, N + 1)}
    for m in range(N - 1):
    	u, v = map(int, raw_input().split())
    	adj[u].add(v)
    	adj[v].add(u)
    seq = []
    for i in range(N - 2):
    	best = N + 1
    	for leaf in range(1, N + 1):
    		if len(adj[leaf]) != 1:
    			continue
    		best = min(best, leaf)
    	other, = adj[best]
    	seq.append(other)
    	adj[other].remove(best)
    	adj[best].remove(other)
    print ' '.join(map(str, seq))
