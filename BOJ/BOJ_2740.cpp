// BOJ_2740
// 행렬 곱셈

#include <algorithm>
#include <cstdint>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);

	int n, m, k;
	cin >> n >> m;
	vector<vector<int>> m1(n, vector<int>(m, 0));

	for (int j = 0; j < n; j++) {
		for (int i = 0; i < m; i++) {
			cin >> m1[j][i];
		}
	}

	cin >> m >> k;
	vector<vector<int>> m2(m, vector<int>(k, 0));

	for (int j = 0; j < m; j++) {
		for (int i = 0; i < k; i++) {
			cin >> m2[j][i];
		}
	}

	vector<vector<int>> res(n, vector<int>(k, 0));

	for (int j = 0; j < n; j++) {
		for (int i = 0; i < k; i++) {
			for (int l = 0; l < m; l++) {
				res[j][i] += m1[j][l] * m2[l][i];
			}
		}
	}

	for (int j = 0; j < n; j++) {
		for (int i = 0; i < k; i++) {
			cout << res[j][i] << ' ';
		}
		cout << '\n';
	}

	return 0;
}
