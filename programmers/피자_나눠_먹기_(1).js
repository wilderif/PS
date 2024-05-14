// 피자_나눠_먹기_(1)

function solution(n) {
    var answer = 0;
    answer = Math.floor(n / 7);
    if (n % 7) {
        answer++;
    }
    return answer;
}