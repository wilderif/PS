// BOJ_10384
// 팬그램

#include <iostream>
#include <cstdint>
#include <algorithm>
#include <string>
#include <vector>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int t = 0;
    cin >> t;
    cin.ignore();

    int c = t;
    while (t--) {
        string s;
        getline(cin, s);

        vector<int> check(26, 0);

        for (char c : s) {
            if ('a' <= c && c <= 'z') {
                check[c - 'a']++;
            } else if ('A' <= c && c <= 'Z') {
                check[c - 'A']++;
            }
        }

        int res = 100;
        for (int i = 0; i < 26; i++) {
            res = min(res, check[i]);
        }

        if (res == 0) {
            cout << "Case " << c - t << ": " << "Not a pangram" << '\n';
        } else if (res == 1) {
            cout << "Case " << c - t << ": " << "Pangram!" << '\n';
        } else if (res == 2) {
            cout << "Case " << c - t << ": " << "Double pangram!!" << '\n';
        } else {
            cout << "Case " << c - t << ": " << "Triple pangram!!!" << '\n';
        }
    }


    return 0;
}
