// 짝수_홀수_개수

function solution(num_list) {
    var answer = [0, 0];
    for (let i of num_list) {
        if (i % 2) {
            answer[1]++;
        } else{
            answer[0]++;
        }
    }
    return answer;
}
