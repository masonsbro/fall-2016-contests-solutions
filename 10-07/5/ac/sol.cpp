#include <iostream>
#include <cstring>
#include <algorithm>
#include <utility>
#include <functional>
#include <vector>
#include <queue>

using namespace std;

int E, F, H;

vector<pair<int, long long> > graph[30003];
int heroes[30003];
long long dist[30003];

void dijkstra() {
    priority_queue<pair<long long, int>, vector<pair<long long, int> >, greater<pair<long long, int> > > pq;
    pq.push(make_pair(0LL, F - 1));

    memset(dist, -1, sizeof(dist));

    while (!pq.empty()) {
        pair<long long, int> cur = pq.top();
        pq.pop();
        long long cur_dist = cur.first;
        int pos = cur.second;

        if (dist[pos] == -1) {
            dist[pos] = cur_dist;

            for (pair<int, long long> next_floor : graph[pos]) {
                int next_loc = next_floor.first;
                long long new_dist = cur_dist + next_floor.second;

                if (dist[next_loc] == -1) {
                    pq.push(make_pair(new_dist, next_loc));
                }
            }
        }
    }
}

int main() {
    int T, S, N;
    string dir;
    cin >> T;
    while (T-- > 0) {
        for (int i = 0; i < 30003; ++i) {
            graph[i].clear();
        }

        cin >> E >> F >> H;
        for (int i = 0; i < E; ++i) {
            cin >> S >> N >> dir;
            long long dist = S * N;
            // Flip the directions
            if (dir == "UP") {
                for (int i = N; i < F; i += N) {
                    graph[i].push_back(make_pair(i - N, dist));
                }
            } else {
                for (int i = 0; i + N < F; i += N) {
                    graph[i].push_back(make_pair(i + N, dist));
                }
            }
        }

        for (int i = 0; i < H; ++i) {
            cin >> heroes[i];
        }

        dijkstra();

        long long ans = -1LL;
        for (int i = 0; i < H; ++i) {
            int hero = heroes[i];
            if (dist[hero] < 0) {
                ans = -1;
                break;
            }
            ans = max(ans, dist[hero]);
        }

        if (ans == -1) {
            cout << "IMPOSSIBLE\n";
        } else {
            cout << ans << '\n';
        }
    }

    return 0;
}
