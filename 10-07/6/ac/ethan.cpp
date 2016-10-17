#include <iostream>
#include <queue>

#define MAX_N 710
#define SOURCE 708
#define SINK 709
#define INF 1000000000

typedef long long ll;

using namespace std;

int T, N, K, S, D, U, V, temp;
vector<int> adj[MAX_N];
ll pos_sum;
ll cap[MAX_N][MAX_N];
int val[MAX_N];

int par[MAX_N];
ll cur_flow[MAX_N];
ll flow[MAX_N][MAX_N];
ll aug, best_flow;

ll my_min(ll a, ll b) {
    return a < b ? a : b;
}

void bfs() {
    for (int i = 0; i < MAX_N; i++) {
        par[i] = -1;
    }
    par[SOURCE] = -2;
    cur_flow[SOURCE] = INF;
    queue<int> q;
    q.push(SOURCE);
    aug = 0;
    while (!q.empty()) {
        int u = q.front(); q.pop();
        for (int i = 0; i < adj[u].size(); i++) {
            int v = adj[u][i];
            if (cap[u][v] - flow[u][v] > 0 && par[v] == -1) {
                par[v] = u;
                cur_flow[v] = my_min(cur_flow[u], cap[u][v] - flow[u][v]);
                if (v != SINK) {
                    q.push(v);
                } else {
                    aug = cur_flow[v];
                    return;
                }
            }
        }
    }
}

void max_flow() {
    best_flow = 0;
    for (int i = 0; i < MAX_N; i++) {
        for (int j = 0; j < MAX_N; j++) {
            flow[i][j] = 0;
        }
    }
    while (true) {
        bfs();
        if (aug == 0) break;
        int v = SINK;
        best_flow += aug;
        while (v != SOURCE) {
            int u = par[v];
            flow[u][v] += aug;
            flow[v][u] -= aug;
            v = u;
        }
    }
}

int main() {
    cin >> T;
    for (int t = 0; t < T; t++) {
        cin >> N >> K >> S >> D;
        // clear adj list
        for (int i = 0; i < MAX_N; i++) {
            adj[i].clear();
        }
        // clear capacity matrix
        for (int i = 0; i < MAX_N; i++) {
            for (int j = 0; j < MAX_N; j++) {
                cap[i][j] = 0;
            }
        }
        // get dependencies and add infinity edges
        for (int d = 0; d < D; d++) {
            cin >> U >> V;
            adj[U].push_back(V);
            adj[V].push_back(U);
            cap[U][V] = INF;
        }
        for (int i = 1; i <= N; i++) {
            cin >> val[i];
            val[i] *= -S;
        }
        for (int i = 1; i <= K; i++) {
            cin >> temp;
            val[i] += temp;
        }
        pos_sum = 0;
        // some of the businesses are positive, some are negative
        for (int i = 1; i <= N; i++) {
            if (val[i] > 0) {
                // if business is +, then add edge source -> business
                adj[SOURCE].push_back(i);
                adj[i].push_back(SOURCE);
                cap[SOURCE][i] = val[i];
                pos_sum += val[i];
            } else if (val[i] < 0) {
                // if business is -, then add edge business -> sink
                adj[i].push_back(SINK);
                adj[SINK].push_back(i);
                cap[i][SINK] = -val[i];
            }
        }
        // now run max flow from source to sink to get
        //     min cut = sum (val[i] when val[i] > 0) - sum (val[i] when i in optimal set)
        // so answer is
        //     sum (val[i] when val[i] > 0) - min cut
        max_flow();
        cout << pos_sum - best_flow << endl;
    }

    return 0;
}
