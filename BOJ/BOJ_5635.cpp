// BOJ_5635
// 생일

#include <iostream>
#include <algorithm>
#include <string>
#include <vector>

using namespace std;

struct student {
    string name;
    int day, month, year;
};

bool compare(student& x, student& y) {
    if (x.year != y.year) {
        return x.year > y.year;
    } else if (x.month != y.month) {
        return x.month > y.month;
    } else {
        return x.day > y.day;
    }
}

int main() {
    cin.tie(NULL);
	ios_base::sync_with_stdio(false);

    int n = 0;
    cin >> n;
    
    vector<student> students(n);

    string tmp_name;
    int tmp_day, tmp_month, tmp_year;
    for (int i = 0; i < n; ++i) {
        cin >> tmp_name >> tmp_day >> tmp_month >> tmp_year;
        students[i].name = tmp_name;
        students[i].day = tmp_day;
        students[i].month = tmp_month;
        students[i].year = tmp_year;
    }

    sort(students.begin(), students.end(), compare);
    
    cout << students[0].name << '\n' << students[n - 1].name;

    return 0;
}