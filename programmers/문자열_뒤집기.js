// 문자열_뒤집기

function solution(my_string) {
  var answer = "";
  for (var i = my_string.length - 1; i >= 0; i--) {
    answer += my_string[i];
  }
  return answer;
}
