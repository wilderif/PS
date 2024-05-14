// BOJ_2167
// 2차원 배열의 합

#include <algorithm>
#include <cstdint>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);

	uint16_t n, m;
	cin >> n >> m;

	vector<vector<int64_t>> arr(n + 1, vector<int64_t>(m + 1, 0));

	for (int j = 1; j < n + 1; j++) {
		for (int i = 1; i < m + 1; i++) {
			cin >> arr[j][i];
			arr[j][i] += arr[j][i - 1];
		}
	}

	uint16_t k;
	cin >> k;

	while (k--) {
		uint16_t i, j, x, y;
		cin >> i >> j >> x >> y;

		int64_t res = 0;
		for (int k = 0; k < x - i + 1; k++) {
			res += arr[i + k][y] - arr[i + k][j - 1];
		}
		cout << res << '\n';
	}

	return 0;
<<<<<<< HEAD
}
=======
}
>>>>>>> 5ae11d8804eca0ee95680c2228111cdb04fcc3ac
