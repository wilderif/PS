// 대문자와_소문자

function solution(my_string) {
  var answer = "";
  for (let c of my_string) {
    if (c === c.toUpperCase()) {
      answer += c.toLowerCase();
    } else {
      answer += c.toUpperCase();
    }
  }
  return answer;
}
