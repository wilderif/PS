// 배열_원소의_길이

function solution(strlist) {
  var answer = [];
  strlist.forEach((str) => {
    answer.push(str.length);
  });
  return answer;
}
