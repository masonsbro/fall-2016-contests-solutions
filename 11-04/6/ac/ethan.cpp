#include <iostream>
#include <cstring>

#define MAX_N 505
#define MAX_B 102

using namespace std;

int T, N, B[MAX_N];
bool dp[MAX_N][MAX_N*MAX_B];

int main() {
    cin >> T;
    while (T--) {
        memset(dp, 0, sizeof(dp));
        cin >> N;
        int total = 0;
        for (int i = 1; i <= N; i++) {
            cin >> B[i];
            total += B[i];
        }
        dp[0][0] = true;
        for (int i = 1; i <= N; i++) {
            for (int j = 0; j <= i*MAX_B; j++) {
                dp[i][j] = dp[i - 1][j];
                if (j >= B[i]) {
                    dp[i][j] |= dp[i - 1][j - B[i]];
                }
            }
        }
        int best = total;
        for (int j = 0; j <= N * MAX_B; j++) {
            if (dp[N][j])
                best = min(best, abs(total - 2*j));
        }
        cout << best << '\n';
    }
    
    return 0;
}
