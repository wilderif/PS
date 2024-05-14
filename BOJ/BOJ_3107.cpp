// BOJ_3107
// IPv6

#include <iostream>
#include <algorithm>
#include <string>
#include <vector>

using namespace std;

int main() {
    cin.tie(NULL);
	ios_base::sync_with_stdio(false);

    string s;
    cin >> s;

    vector<string> res;
    
    int sep_cnt = 0;
    for (int i = 0; i < s.size(); ++i) {
        if (s[i] == ':' && s[i + 1] == ':') {
            sep_cnt++;
            i++;
        } else if (s[i] == ':') {
            sep_cnt++;
        }
    }

    if (s.size() == 2) {
        for (int i = 0; i < 8; ++i) {
            res.push_back("0000");
        }
    } else if (s[0] == ':' && s[1] == ':') {
        string tmp = "";
        for (int i = 0; i < s.size(); ++i) {
            if (s[i] == ':' && s[i + 1] == ':') {
                for (int j = 0; j < 8 - sep_cnt; ++j) {
                    res.push_back("0000");
                }
                i++;
            } else if (s[i] == ':') {
                res.push_back(tmp);
                tmp = "";
            } else {
                tmp += s[i];
            }
            if (i == s.size() - 1) {
               res.push_back(tmp);
            }
        }
    } else if (s[s.size() - 1] == ':' && s[s.size() - 2] == ':') {
        string tmp = "";
        for (int i = 0; i < s.size(); ++i) {
            if (s[i] == ':' && s[i + 1] == ':') {
                res.push_back(tmp);
                tmp = "";
                for (int j = 0; j < 8 - sep_cnt; ++j) {
                    res.push_back("0000");
                }
                i++;
            } else if (s[i] == ':') {
                res.push_back(tmp);
                tmp = "";
            } else {
                tmp += s[i];
            }
        }
    } else {
        string tmp = "";
        for (int i = 0; i < s.size(); ++i) {
            if (s[i] == ':' && s[i + 1] == ':') {
                res.push_back(tmp);
                tmp = "";
                for (int j = 0; j < 8 - sep_cnt - 1; ++j) {
                    res.push_back("0000");
                }
                i++;
            } else if (s[i] == ':') {
                res.push_back(tmp);
                tmp = "";
            } else {
                tmp += s[i];
            }
            if (i == s.size() - 1) {
               res.push_back(tmp);
            }
        }
    }

    for (int i = 0; i < res.size(); ++i) {
        int tmp = 4 - res[i].size();

        while (tmp--) {
                res[i] = "0" + res[i];     
        }
    }

    for (int i = 0; i < 7; ++i) {
        if (res[i] == "") {
            continue;
        }
        cout << res[i] << ':';
    }
    cout << res[7];
      
    return 0;
}