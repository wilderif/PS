// 문자열_섞기

function solution(str1, str2) {
    var answer = '';
    let res = new Array
    for (let i = 0; i < str1.length + str2.length; i++) {
        if (i % 2) {
            res.push(str2[Math.floor(i / 2)]);
        } else {
            res.push(str1[Math.floor(i / 2)]);
        }
    }
    answer = res.join('')
    return answer;
}
