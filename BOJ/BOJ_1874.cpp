// BOJ_1874
// 스택 수열

#include <iostream>
#include <algorithm>
#include <cstdint>
#include <string>
#include <vector>
#include <stack>

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

	stack<int> s;
	string res = "";
	int arr_idx = 0;
	for (int i = 1; i < n + 1; i++) {
		while (!s.empty() && s.top() == arr[arr_idx]) {
			s.pop();
			res += "-\n";
			arr_idx++;
		}
		s.push(i);
		res += "+\n";
	}
	while (!s.empty() && s.top() == arr[arr_idx]) {
		s.pop();
		res += "-\n";
		arr_idx++;
	}

	if (s.empty()) {
		cout << res;
	} else {
		cout << "NO";
	}

	return 0;
<<<<<<< HEAD
}
=======
}
>>>>>>> 5ae11d8804eca0ee95680c2228111cdb04fcc3ac
