#include <iostream>
#include <iomanip>
#include <cstring>
#include <algorithm>
#include <utility>

using namespace std;

int m, n;
int matrix[1003];
int a[1003 * 1003];
int ia[1003];
int ja[1003 * 1003];

void read_input() {
    cin >> m >> n;
    for (int i = 0; i <= m; ++i) {
        cin >> ia[i];
    }
    int l = ia[m];
    for (int i = 0; i < l; ++i) {
        cin >> a[i];
    }
    for (int i = 0; i < l; ++i) {
        cin >> ja[i];
    }
}

int main() {
    int T;
    cin >> T;
    while (T-- > 0) {
        read_input();

        int a_ptr = 0;

        for (int row = 0; row < m; ++row) {
            memset(matrix, 0, sizeof(matrix));
            int num_in_row = ia[row + 1] - ia[row];

            for (int k = 0; k < num_in_row; ++k) {
                matrix[ja[a_ptr]] = a[a_ptr];
                a_ptr++;
            }

            cout << matrix[0];
            for (int col = 1; col < n; ++col) {
                cout << ' ' << matrix[col];
            }
            cout << '\n';
        }
    }

    return 0;
}
