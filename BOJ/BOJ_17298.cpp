// BOJ_17298
// 오큰수

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

	vector<int> res(n, 0);
	vector<int> stack;
	for (int i = 0; i < n; i++) {
		while (!stack.empty() && stack[stack.size() - 1] <= arr[n - i - 1]) {
			stack.pop_back();

		}
		if (stack.empty()) {
			res[n - i - 1] = -1;
		} else {
			res[n - i - 1] = stack[stack.size() - 1];
		}
		stack.push_back(arr[n - i - 1]);
	}

	for (int i = 0; i < n; i++) { 
		cout << res[i] << ' ';
	}

	return 0;
<<<<<<< HEAD
}
=======
}
>>>>>>> 5ae11d8804eca0ee95680c2228111cdb04fcc3ac
