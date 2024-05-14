// 최빈값_구하기

function solution(array) {
    var answer = 0;
    let arr = Array.from({length : 1000}, () => 0);
    for (let i of array) {
        arr[i] += 1;
    }
    let flag = false;
    max_val = 0;
    for (let i = 0; i < 1000; i++) {
        if (arr[i] > max_val) {
            max_val = arr[i];
            answer = i;
            flag = true;
        }
        else if (arr[i] === max_val) {
            flag = false;
        }
    }
    if (!flag) {
        return -1;
    }
    return answer;
}