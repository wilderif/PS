// x만큼_간격이_있는_n개의_숫자

function solution(x, n) {
  const res = [];
  for (let i = 0; i < n; i++) {
    res.push(x * (i + 1));
  }
  return res;
}
