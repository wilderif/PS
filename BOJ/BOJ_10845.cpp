// BOJ_10845
// 큐

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
	
	int arr[10001];
	int head = 0, tail = 0;

	int n = 0;
	cin >> n;
	while (n--) {
		string inst;
		cin >> inst;
		if (inst == "push") {
			int tmp = 0;
			cin >> arr[tail++];
		} else if (inst == "pop") {
			if (head == tail) {
				cout << -1 << '\n';
			} else {
				cout << arr[head++] << '\n';
			}
		} else if (inst == "size") {
			cout << tail - head << '\n';
		} else if (inst == "empty") {
			cout << (head == tail) << '\n';
		} else if (inst == "front") {
			if (head == tail) {
				cout << -1 << '\n';
			} else {
				cout << arr[head] << '\n';
			}
		} else if (inst == "back") {
			if (head == tail) {
				cout << -1 << '\n';
			} else {
				cout << arr[tail - 1] << '\n';
			}
		}
	}

	return 0;
<<<<<<< HEAD
}
=======
}
>>>>>>> 5ae11d8804eca0ee95680c2228111cdb04fcc3ac
