// 짝수는_싫어요

function solution(n) {
    var answer = [];
    for (let i = 1; i <= n; i++) {
        if (i % 2) {
            answer.push(i)
        }
    }
    return answer;
}
