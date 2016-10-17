#include <iostream>
#include <string>
#include <cstring>
#include <algorithm>
#include <utility>
#include <vector>
#include <map>
#include <set>

#define MAXN 100005

using namespace std;

int N, K;
string gadgets[MAXN];
set<string> dedupe;

bool works(int window_size) {
    map<string, int> freq_map;
    for (int i = 0; i < window_size; ++i) {
        freq_map[gadgets[i]] += 1;
    }

    for (int i = window_size; i < N; ++i) {
        if (freq_map.size() >= K) {
            return true;
        }

        freq_map[gadgets[i]] += 1;
        freq_map[gadgets[i - window_size]] -= 1;
        if (freq_map[gadgets[i - window_size]] == 0) {
            freq_map.erase(freq_map.find(gadgets[i - window_size]));
        }
    }

    return freq_map.size() >= K;
}

int main() {
    int T;
    cin >> T;
    while (T-- > 0) {
        dedupe.clear();
        cin >> N >> K;
        for (int i = 0; i < N; ++i) {
            cin >> gadgets[i];
            dedupe.insert(gadgets[i]);
        }

        if (K == 1) {
            cout << 1 << '\n';
        } else if ((int)dedupe.size() < K) {
            cout << -1 << '\n';
        } else {
            int lo = 1;
            int hi = N;
            while (lo + 1 < hi) {
                int mid = (lo + hi) >> 1;
                if (works(mid)) {
                    hi = mid;
                } else {
                    lo = mid;
                }
            }

            cout << hi << '\n';
        }
    }
    return 0;
}
