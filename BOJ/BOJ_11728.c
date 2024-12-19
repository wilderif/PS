// BOJ_11728
// 배열 합치기


#include <stdio.h>

int main()
{
    int n, m;
    scanf("%d %d", &n, &m);

    int a[n], b[m], out[n + m];
    for (int i = 0; i < n; ++i)
        scanf("%d", &a[i]);
    for (int i = 0; i < m; ++i)
        scanf("%d", &b[i]);

    int a_idx = 0, b_idx = 0;
    while (a_idx + b_idx < n + m) {
        if (b_idx == m) {
            out[a_idx + b_idx] = a[a_idx];
            a_idx++;
        } else if (a_idx == n) {
            out[a_idx + b_idx] = b[b_idx];
            b_idx++;
        } else if (a[a_idx] <= b[b_idx]) {
            out[a_idx + b_idx] = a[a_idx];
            a_idx++;
        } else {
            out[a_idx + b_idx] = b[b_idx];
            b_idx++;
        }
    }

    for (int i = 0; i < n + m; ++i)
        printf("%d ", *(out + i));

    return 0;
}
