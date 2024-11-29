// 등수_매기기

function solution(score) {
  for (let i = 0; i < score.length; i++) {
    score[i] = [score[i][0] + score[i][1], i];
  }
  score = score.sort((a, b) => b[0] - a[0]);
  const res = new Array(score.length);
  let streak = 0;
  for (let i = 0; i < score.length; i++) {
    if (i) {
      if (score[i][0] === score[i - 1][0]) {
        streak += 1;
      } else {
        streak = 0;
      }
    }

    res[score[i][1]] = i - streak + 1;
  }
  return res;
}
