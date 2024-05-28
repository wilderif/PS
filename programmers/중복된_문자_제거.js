// 중복된_문자_제거

function solution(my_string) {
  var answer = "";
  let used = [];
  my_string.split("").forEach((val) => {
    if (used.indexOf(val) === -1) {
      used.push(val);
      answer += val;
    }
  });
  return answer;
}
