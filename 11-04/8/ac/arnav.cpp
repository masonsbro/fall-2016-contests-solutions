#include <iostream>
#include <cstring>
#include <algorithm>
#include <utility>
#include <vector>

using namespace std;

int nodes, edges;
long long targetSpeed;
int dist[155];
bool visit[155];
vector<pair<int, int> > graph[155];

const int INF = 0x3fffffff;

void dfs(int node) {
    if (visit[node]) return;
    visit[node] = true;
    for (pair<int, int> edge : graph[node]) {
        dfs(edge.first);
    }
}

int main() {
    int T;
    cin >> T;

    while (T-- > 0) {
        cin >> nodes >> edges >> targetSpeed;
        for (int i = 0; i < nodes; ++i) {
            graph[i].clear();
            dist[i] = INF;
            visit[i] = false;
        }

        int start, end, weight;
        for (int i = 0; i < edges; ++i) {
            cin >> start >> end >> weight;
            --start;
            --end;

            graph[start].push_back(make_pair(end, -weight));
        }

        // Run Bellman ford
        dist[0] = 0;
        for (int iter = 0; iter < nodes - 1; ++iter) {
            for (int node = 0; node < nodes; ++node) {
                if (dist[node] == INF) {
                    continue;
                }

                for (pair<int, int> edge : graph[node]) {
                    int destination = edge.first;
                    int weight = edge.second;
                    dist[destination] = min(dist[destination], dist[node] + weight);
                }
            }
        }

        // find the negative cycle.
        for (int node = 0; node < nodes; ++node) {
            for (pair<int, int> edge : graph[node]) {
                int destination = edge.first;
                int weight = edge.second;
                if (dist[node] + weight < dist[destination]) {
                    dfs(destination);
                }
            }
        }

        cout << (visit[nodes - 1] ? "YES" : "NO") << '\n';
    }

    return 0;
}
