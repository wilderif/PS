// 피자_나눠_먹기_(2)

function solution(n) {
    var answer = 0;
    while (1) {
        answer++;
        if ((answer * 6) % n === 0) {
            break;
        }
    }
    return answer;
}