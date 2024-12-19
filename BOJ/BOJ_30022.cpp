// BOJ_30022
// 행사 준비

#include <algorithm>
#include <cstdint>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);

	int n, a, b;
	cin >> n >> a >> b;

	vector<int32_t> d(n, 0);
	vector<int32_t> j(n, 0);
	vector<vector<int32_t>> diff(n, vector<int32_t>(2, 0));

	for (int i = 0; i < n; i++) {
		cin >> d[i] >> j[i];
		diff[i][1] = i;
		diff[i][0] = d[i] - j[i];
	}

	sort(diff.begin(), diff.end());

	uint64_t res = 0;
	for (int i = 0; i < a; i++) {
		res += d[diff[i][1]];
	}

	for (int i = a; i < n; i++) {
		res += j[diff[i][1]];
	}

	cout << res;

	return 0;
}
