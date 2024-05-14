// BOJ_6198
// 옥상 정원 꾸미기

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

	vector<int> arr(n, 0);
	for (int i = 0; i < n; i++) {
		cin >> arr[i];
	}

	long long res = 0;
	vector<vector<int>> stack;
	for (int i = 0; i < n; i++) {
		vector<int> tmp = {arr[n - 1 - i], 0};
		while (!stack.empty() && stack[stack.size() - 1][0] < tmp[0]) {
			res += stack[stack.size() - 1][1] + 1;
			tmp[1] += stack[stack.size() - 1][1] + 1;
			stack.pop_back();
		}
		stack.push_back(tmp);
	}

	cout << res;

	return 0;
}