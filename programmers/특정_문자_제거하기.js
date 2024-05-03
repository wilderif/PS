// 특정_문자_제거하기

function solution(my_string, letter) {
    var answer = '';
    for (let c of my_string) {
        if (c !== letter) {
            answer += c;
        }
    }
    return answer;
}
