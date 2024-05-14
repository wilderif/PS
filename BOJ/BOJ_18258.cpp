// BOJ_18258
// 큐 2

#include <iostream>
#include <algorithm>
#include <cstdint>
#include <string>
#include <vector>
#include <utility>
#include <queue>

using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);
	
	queue<int> arr;

	int n = 0;
	cin >> n;
	while (n--) {
		string inst;
		cin >> inst;
		if (inst == "push") {
			int tmp = 0;
			cin >> tmp;
			arr.push(tmp);
		} else if (inst == "pop") {
			if (arr.empty()) {
				cout << -1 << '\n';
			} else {
				cout << arr.front() << '\n';
				arr.pop();
			}
		} else if (inst == "size") {
			cout << arr.size() << '\n';
		} else if (inst == "empty") {
			cout << arr.empty() << '\n';
		} else if (inst == "front") {
			if (arr.empty()) {
				cout << -1 << '\n';
			} else {
				cout << arr.front() << '\n';
			}
		} else if (inst == "back") {
			if (arr.empty()) {
				cout << -1 << '\n';
			} else {
				cout << arr.back() << '\n';
			}
		}
	}

	return 0;
<<<<<<< HEAD
}
=======
}
>>>>>>> 5ae11d8804eca0ee95680c2228111cdb04fcc3ac
