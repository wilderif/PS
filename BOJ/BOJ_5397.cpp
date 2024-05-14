// BOJ_5397
// 키로거

#include <iostream>
#include <algorithm>
#include <cstdint>
#include <string>
#include <vector>
#include <list>
#include <utility>

using namespace std;


int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);

	int t = 0;
	cin >> t;

	while (t--) {
		string l;
		cin >> l;
		list<char> container;
		list<char>::iterator cursor = container.end();
		for (char c : l) {
			if (c == '<') {
				if (cursor != container.begin()) {
					cursor--;
				}
			} else if (c == '>') {
				if (cursor != container.end()) {
					cursor++;
				}
			} else if (c == '-') {
				if (cursor != container.begin()) {
					cursor--;
					cursor = container.erase(cursor);
				}
			} else {
				container.insert(cursor, c);
			}
		}
		for (char c : container) {
			cout << c;
		}
		cout << '\n';
	}

	return 0;
<<<<<<< HEAD
}
=======
}
>>>>>>> 5ae11d8804eca0ee95680c2228111cdb04fcc3ac
