// 7의_개수

function solution(array) {
  var answer = 0;
  array.forEach((val) => {
    answer += val
      .toString()
      .split("")
      .filter((c) => c === "7").length;
  });
  return answer;
}
