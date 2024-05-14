// BOJ_15649
// N과 M (1)

#include <iostream>
#include <algorithm>
#include <cstdint>
#include <string>
#include <vector>

using namespace std;


void backtracking (int k, const int& n, const int& m, vector<int>& arr, vector<bool>& isused) {
	if (k == m)	{
		for (int i = 0; i < m; i++) {
			cout << arr[i] << ' ';
		}
		cout << '\n';
		return;
	}
	for (int i = 1; i <= n; i++) {
		if (!isused[i]) {
			arr[k] = i;
			isused[i] = true;
			backtracking (k + 1, n, m, arr, isused);
			isused[i] = false;
		}
	}
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);

	int n, m;
	cin >> n >> m;

	vector<int> arr(10, 0);
	vector<bool> isused(10, false);

	backtracking(0, n, m, arr, isused);
	
	return 0;
<<<<<<< HEAD
}
=======
}
>>>>>>> 5ae11d8804eca0ee95680c2228111cdb04fcc3ac
