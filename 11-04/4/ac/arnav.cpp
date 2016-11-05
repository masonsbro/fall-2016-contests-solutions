#include <iostream>
#include <vector>
#include <set>

using namespace std;

int n;
vector<int> tree[1003];
int degree[1003];
set<int> leaf;
set<int> erased;
vector<int> ans;

int main() {
    int T;
    cin >> T;
    int u, v;
    while (T-- > 0) {
        cin >> n;

        memset(degree, 0, sizeof(degree));
        for (int i = 0; i < n; ++i) {
            tree[i].clear();
        }
        leaf.clear();
        erased.clear();
        ans.clear();

        for (int i = 0; i < n - 1; ++i) {
            cin >> u >> v;
            --u;
            --v;

            tree[u].push_back(v);
            tree[v].push_back(u);

            ++degree[u];
            ++degree[v];
        }

        for (int i = 0; i < n; ++i) {
            if (degree[i] == 1) {
                leaf.insert(i);
            }
        }

        for (int nodes = n; nodes > 2; --nodes) {
            // find the smallest leaf node
            int node = *(leaf.begin());
            leaf.erase(leaf.begin());

            --degree[node];
            erased.insert(node);
            int output;
            for (int neighbor : tree[node]) {
                if (erased.find(neighbor) == erased.end()) {
                    output = neighbor;
                    break;
                }
            }

            --degree[output];
            ans.push_back(output + 1);
            if (degree[output] == 1) {
                leaf.insert(output);
            }
        }

        cout << ans[0];
        for (int i = 1; i < n - 2; ++i) {
            cout << ' ' << ans[i];
        }
        cout << '\n';
    }

    return 0;
}
