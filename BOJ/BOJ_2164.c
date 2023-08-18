// BOJ_2164
// 카드2

#include <stdio.h>

void action(int arr[], int start, int end)
{
    arr[end + 1] = arr[start + 1];
}

int main()
{
    int n;
    scanf("%d", &n);
    int start = 0;
    int end = n - 1;
    int card[2 * n];

    for (int i = 0; i < n; ++i) {
        card[i] = i + 1;
    }

    while(start != end) {
        action(card, start, end);
        start += 2;
        end++;
    }

    printf("%d", card[start]);

    return 0;
}
