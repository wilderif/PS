// BOJ_11931
// 수 정렬하기 4

#include <iostream>
#include <algorithm>
#include <cstdint>
#include <string>
#include <vector>

using namespace std;

void merge(vector<int>& arr, int s, int e) {
	int mid = (s + e) / 2;
	int idx1 = s;
	int idx2 = mid;
	vector<int>	tmp(e - s);

	for (int i = 0; i < e - s; i++) {
		if (idx1 == mid) {
			tmp[i] = arr[idx2++];
		} else if (idx2 == e) {
			tmp[i] = arr[idx1++];
		} else if (arr[idx1] >= arr[idx2]) {
			tmp[i] = arr[idx1++];
		} else if (arr[idx1] < arr[idx2]) {
			tmp[i] = arr[idx2++];
		}
	}

	for (int i = 0; i < e - s; i++) {
		arr[s + i] = tmp[i];
	}
}

void merge_sort(vector<int>& arr, int s, int e) {
	if (s + 1 == e) {
		return;
	}
	int mid = (s + e) / 2;
	merge_sort(arr, s, mid);
	merge_sort(arr, mid, e);
	merge(arr, s, e);
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);
	int n = 0;
	cin >> n;
	vector<int> arr(n);

	for (int i = 0; i < n; i++) {
		cin >> arr[i];
	}

	merge_sort(arr, 0, n);
	for (int i = 0; i < n; i++) {
		cout << arr[i] << '\n';
	}

	return 0;
}
