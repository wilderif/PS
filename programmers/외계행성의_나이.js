// 외계행성의_나이

function solution(age) {
  var answer = '';
  age = age.toString();
  for (let c of age) {
    answer += String.fromCharCode(c.charCodeAt() - '0'.charCodeAt() + 'a'.charCodeAt());
  }
  return answer;
}