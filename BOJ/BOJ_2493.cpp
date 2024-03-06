// BOJ_2493
// 탑

#include <iostream>
#include <algorithm>
#include <cstdint>
#include <string>
#include <vector>
#include <utility>

using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);
	
	int n = 0;
	cin >> n;
	
	vector<vector<int>> arr(0, vector<int> (2, 0));
	for (int i = 0; i < n; i++) {
		int tmp;
		cin >> tmp;

		while (!arr.empty() && arr[arr.size() - 1][0] < tmp) {
			arr.pop_back();
		}
		if (arr.empty()) {
				cout << 0 << ' ';
		} else {
			cout << arr[arr.size() - 1][1] << ' ';
		}

		arr.push_back(vector<int> {tmp, i + 1});
	}
	
	return 0;
}
