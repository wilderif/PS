// 피자_나눠_먹기_(3)

function solution(slice, n) {
    var answer = 0;
    while (1) {
        answer++;
        if ((answer * slice) >= n) {
            break;
        }
    }
    return answer;
}