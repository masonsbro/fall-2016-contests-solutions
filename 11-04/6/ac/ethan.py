MAX_B = 75

T = int(raw_input())

for t in range(T):
    N = int(raw_input())
    B = map(int, raw_input().split())
    # dp[i][j] = True iff there is a subset of the first i pins with sum j
    dp = [[False]*(N*MAX_B + 1) for _ in range(N + 1)]
    dp[0][0] = True
    for i in range(1, N + 1):
        for j in range(i*MAX_B + 1):
            dp[i][j] = dp[i - 1][j]
            if j >= B[i - 1] and dp[i - 1][j - B[i - 1]]:
                dp[i][j] = True
    total = sum(B)
    best = sum(B)
    for j in range(N*MAX_B + 1):
        if dp[N][j]:
            best = min(best, abs(total - 2 * j))
    print best
