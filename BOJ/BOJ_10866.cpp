// BOJ_10866
// 덱

#include <iostream>
#include <algorithm>
#include <cstdint>
#include <string>
#include <vector>

using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);

	int max = 10000;
	int dq[max * 2 + 1];
	int head = max, tail = max;
	
	int n = 0;
	cin >> n;
	while (n--) {
		string inst;
		cin >> inst;
		if (inst == "push_front") {
			cin >> dq[--head];
		} else if (inst == "push_back") {
			cin >> dq[tail++];
		} else if (inst == "pop_front") {
			if (head == tail) {
				cout << -1 << '\n';
			} else {
				cout << dq[head++] << '\n';
			}
		} else if (inst == "pop_back") {
			if (head == tail) {
				cout << -1 << '\n';
			} else {
				cout << dq[--tail] << '\n';
			}
		} else if (inst == "size") {
			cout << tail - head << '\n';
		} else if (inst == "empty") {
			cout << (head == tail) << '\n';
		} else if (inst == "front") {
			if (head == tail) {
				cout << -1 << '\n';
			} else {
				cout << dq[head] << '\n';
			}
		} else if (inst == "back") {
			if (head == tail) {
				cout << -1 << '\n';
			} else {
				cout << dq[tail - 1] << '\n';
			}
		}
	}

	return 0;
}
