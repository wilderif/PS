// BOJ_2108
// 통계학

#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int compare(const void *a, const void *b);
void input_sort(int arr[], int n);
double arithmetic_mean(int arr[], int n);
int median(int arr[], int n);
int mode(int arr[], int n);
int range(int arr[], int n);

int main()
{
    int n;
    scanf("%d", &n);
    int numbers[n];
    for (int i = 0; i < n; ++i) {
        numbers[i] = 4001;
    }

    input_sort(numbers, n);

    printf("%d\n", (int)(round(arithmetic_mean(numbers, n))));
    printf("%d\n", median(numbers, n));
    printf("%d\n", mode(numbers, n));
    printf("%d\n", range(numbers, n));

    return 0;
}

int compare(const void *a, const void *b)
{
    return (*(int *)a - *(int *)b);
}

void input_sort(int arr[], int n)
{
    for (int i = 0; i < n; ++i )
        scanf("%d", &arr[i]);

    qsort(arr, n, sizeof(int), compare);
}

double arithmetic_mean(int arr[], int n)
{
    double sum = 0;
    for (int i = 0; i < n; ++i) {
        sum += arr[i];
    }
    return sum / (double )n;
}

int median(int arr[], int n)
{
    return arr[n / 2];
}

//int mode(int arr[], int n)
//{
//    if (n == 1)
//        return arr[0];
//
//    int arr_mode[n][2];
//    for (int i = 0; i < n; ++i) {
//        arr_mode[i][0] = 4001;
//        arr_mode[i][1] = 0;
//    }
//
//    int mode_idx[2] = {0, -1};
//
//    for (int i = 0; i < n; ++i) {
//        for (int j = 0; j < n; ++j) {
//            if (arr_mode[j][0] == 4001) {
//                arr_mode[j][0] = arr[i];
//                arr_mode[j][1]++;
//                break;
//            }
//            if (arr[i] == arr_mode[j][0]) {
//                arr_mode[j][1]++;
//                break;
//            }
//        }
//    }
//
//    for (int i = 1; i < n; ++i) {
//        if (arr_mode[i][1] > arr_mode[mode_idx[0]][1])
//            mode_idx[0] = i;
//        else if (mode_idx[1] == -1 || (arr_mode[i][1] == arr_mode[mode_idx[0]][1] && arr_mode[i][1] > arr_mode[mode_idx[1]][1]))
//            mode_idx[1] = i;
//    }
//
//    if (arr_mode[mode_idx[0]][1] == arr_mode[mode_idx[1]][1])
//        return arr_mode[mode_idx[1]][0];
//    else
//        return arr_mode[mode_idx[0]][0];
//}

int mode(int arr[], int n)
{
    if (n == 1)
        return arr[0];
    int frequency[8001] = {0};
    int mode_num = 0;
    int first_idx = -1;
    int second_idx = -1;

    for (int i = 0; i < n; ++i) {
        frequency[arr[i] + 4000]++;
    }

    for (int i = 0; i < 8001; ++i) {
        if (frequency[i] > mode_num) {
            mode_num = frequency[i];
            first_idx = i;
        } else if (frequency[i] == mode_num && (second_idx == -1 || frequency[second_idx] < frequency[i])) {
            second_idx = i;
        }

    }

    if (frequency[first_idx] > frequency[second_idx])
        return first_idx - 4000;
    return second_idx - 4000;
}

int range(int arr[], int n)
{
    return arr[n - 1] - arr[0];
<<<<<<< HEAD
}
=======
}
>>>>>>> 5ae11d8804eca0ee95680c2228111cdb04fcc3ac
