#include <iostream>
#include <sstream>
#include <cstring>
#include <string>
#include <algorithm>
#include <utility>
#include <vector>
#include <map>

using namespace std;

int n, m;

int q, id, range_start, range_end;
map<string, vector<int> > lookup;
map<int, vector<pair<int, int> > > intervals;

int main() {
    int T;
    cin >> T;
    string s, tag;

    while (T-- > 0) {
        cin >> n >> m >> q;

        lookup.clear();
        intervals.clear();

        for (int i = 0; i < n; ++i) {
            vector<string> tags;
            cin >> id;

            getline(cin, s);
            getline(cin, s);
            istringstream iss(s);

            while (iss >> tag) {
                lookup[tag].push_back(id);
            }
        }

        int max_time = 0;
        for (int i = 0; i < m; ++i) {
            cin >> id >> range_start >> range_end;
            intervals[id].push_back(make_pair(range_start, range_end));
            max_time = max(max_time, range_end);
        }

        for (int i = 0; i < q; ++i) {
            cin >> tag;
            int ans = 0;
            for (int time = 0; time <= max_time; ++time) {
                // see if there's a pin with the tag at this time
                bool found = false;
                for (int id : lookup[tag]) {
                    if (found) break;
                    for (pair<int, int> interval : intervals[id]) {
                        if (found) break;
                        found |= (interval.first <= time and time <= interval.second);
                    }
                }

                if (found) {
                    ++ans;
                }
            }

            cout << ans << '\n';
        }
    }
    return 0;
}
