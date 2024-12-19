// BOJ_30825
// 건공펀치 등차수열

#include <algorithm>
#include <cstdint>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);

	int n, k;
	cin >> n >> k;
	
	vector<int> arr(n, 0);

	for (size_t i = 0; i < n; i++) {
		cin >> arr[i];
	}

	uint64_t res = 0, ex_num = arr[0];
	for (size_t i = 1; i < n; i++) {
		if (arr[i] <= ex_num + k) {
			res += ex_num + k - arr[i];
			ex_num = ex_num + k;
		} else {
			res += (arr[i] - ex_num - k) * i;
			ex_num = arr[i];
		}
	}

	cout << res;

	return 0;
}
