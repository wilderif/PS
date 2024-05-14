// BOJ_28278
// 스택 2

#include <iostream>
#include <algorithm>
#include <cstdint>
#include <string>
#include <vector>
#include <list>
#include <utility>

using namespace std;

void push(int arr[], int& pos, int x) {
	pos++;
	arr[pos] = x;
}

void pop(int arr[], int& pos) {
	if (!pos) {
		cout << -1 << '\n';
	} else {
		cout << arr[pos] << '\n';
		pos--;
	}
}

void top(int arr[], int& pos) {
	if (pos) {
		cout << arr[pos] << '\n';
	} else {
		cout << -1 << '\n';
	}
}


int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);

	int stack[1000005];
	int pos = 0;
	
	int n = 0;
	cin >> n;

	while (n--) {
		int inst;
		cin >> inst;
		if (inst == 1) {
			int tmp;
			cin >> tmp;
			push(stack, pos, tmp);
		} else if (inst == 2) {
			pop(stack, pos);
		} else if (inst == 3) {
			cout << pos << '\n';
		} else if (inst == 4) {
			if (pos) {
				cout << 0 << '\n';
			} else {
				cout << 1 << '\n';
			}
		} else if (inst == 5) {
			top(stack, pos);
		}
	}

	return 0;
<<<<<<< HEAD
}
=======
}
>>>>>>> 5ae11d8804eca0ee95680c2228111cdb04fcc3ac
