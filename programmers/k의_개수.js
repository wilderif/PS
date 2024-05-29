// k의_개수

function solution(i, j, k) {
  var answer = 0;
  for (let idx = i; idx <= j; idx++) {
    idx
      .toString()
      .split("")
      .forEach((val) => {
        answer += val
          .toString()
          .split("")
          .filter((c) => c === k.toString()).length;
      });
  }
  return answer;
}
